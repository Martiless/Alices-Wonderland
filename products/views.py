from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ManageProductsForm


def all_products(request):
    """
    This view will show all the products as well
    as sorting and search options
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:

        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
                products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter a search term!")
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_details(request, product_id):
    """
    This view will show the details of each
    product when a user clicks on it
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_details.html', context)


def add_product(request):
    """ Adding products to the store """
    if request.method == 'POST':
        form = ManageProductsForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'New products has been successfully added!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Product was not added. Please check form and try again!')
    else:
        form = ManageProductsForm()

    template = 'products/add_products.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_product(request, product_id):
    """ Editing Products on the store """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ManageProductsForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, f'You have updated {product.name}')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            messages.error(request, 'Product was not updated. Please check form and try again!')
    else:
        form = ManageProductsForm(instance=product)
        messages.info(request, f'Please note you are about to edit {product.name}')

    template = 'products/edit_products.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


def delete_product(request, product_id):
    """Delete products from the store """
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'You have deleted {product.name}')
    return redirect(reverse('products'))
