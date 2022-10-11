from django.shortcuts import render
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
