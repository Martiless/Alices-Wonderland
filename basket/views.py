from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def basket(request):
    """
    This view will display the shoppers basket
    """

    return render(request, 'basket/basket.html')


def add_to_basket(request, item_id):
    """
    This view will add the quantity selected
    for a product to the basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    basket = request.session.get('basket', {})

    if item_id in list(basket.keys()):
        basket[item_id] += quantity
        messages.success(
            request, f'You have updated {product.name} in your basket. Quantity is no {basket[item_id]}')
    else:
        basket[item_id] = quantity

    request.session['basket'] = basket
    return redirect(redirect_url)


def update_basket(request, item_id):
    """
    This view will update the products
    in the bag when a user clicks on the
    update link
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    basket = request.session.get('basket', {})

    if quantity > 0:
        basket[item_id] = quantity
        messages.success(
            request, f'You have updated {product.name} in your basket. Quantity is no {basket[item_id]}')
    else:
        basket.pop(item_id)
        messages.success(
            request, f'You have successfully removed {product.name} from your basket')

    request.session['basket'] = basket
    return redirect(reverse('basket'))


def delete_from_basket(request, item_id):
    """
    This view will delete the products
    in the bag when a user clicks on the
    update link
    """

    product = get_object_or_404(Product, pk=item_id)
    basket = request.session.get('basket', {})
    
    try:
        basket.pop(item_id)
        messages.success(
            request, f'You have successfully removed {product.name} from your basket')

        request.session['basket'] = basket
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
