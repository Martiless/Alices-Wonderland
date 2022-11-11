from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ManageProductsForm, ReviewForm


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
    template = 'products/product_details.html'
    form = ReviewForm()
    reviews = []

    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            review = form.save(commit=False)
            review.reviewer = request.user
            review.product = product
            review.save()
            messages.success(request, 'Thank you for your review. It is currently under review!')
            return redirect(reverse('product_details', args=[product.id]))
        else:
            form = ReviewForm()

    context = {
        'product': product,
        'form': form,
        'reviews': reviews,
    }

    return render(request, template, context)


@login_required
def add_product(request):
    """ Adding products to the store """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the authority to access this page!')
        return redirect(reverse('home'))

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


@login_required
def edit_product(request, product_id):
    """ Editing Products on the store """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the authority to access this page!')
        return redirect(reverse('home'))

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


@login_required
def delete_product(request, product_id):
    """Delete products from the store """
    if not request.user.is_superuser:
        messages.error(request, 'You do not have the authority to access this page!')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, f'You have deleted {product.name}')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """ Adding reviews to products """

    product = get_object_or_404(Product, pk=product_id)

    form = ReviewForm(data=request.POST)
    if form.is_valid():
        review = form.save(commit=False)
        review.user = request.user
        review.product = product
        form.save()
        messages.success(request, 'Thank you for your review. It is currently under review!')
        return redirect(reverse('product_details', args=[product.id]))
    else:
        form = ReviewForm()

    template = 'products/add_review.html'
    context = {
        'form': form,
        'reviewed': True,
    }

    return render(request, template, context)