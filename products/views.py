from django.shortcuts import render, get_object_or_404
from .models import Product


def all_products(request):
    """
    This view will show all the products as well
    as sorting and search options
    """

    products = Product.objects.all()

    context = {
        'products': products,
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
