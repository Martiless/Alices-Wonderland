from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
import stripe
from basket.contexts import basket_contents
from products.models import Product
from .forms import OrderForm
from .models import Order, OrderLineItems



def checkout(request):
    """
    Checkout View
    """
    stripe_public_key = settings.SRTIPE_PUBLIC_KEY
    stripe_secret_key = settings.SRTIPE_SECRET_KEY

    if request.method == 'POST':
        basket = request.session.get('basket', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email_address': request.POST['email_address'],
            'phone': request.POST['phone'],
            'country': request.POST['country'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for item_id, item_data in basket.items():
                try:
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItems(
                            order=order,
                            product=product,
                            quantity=item_data
                        )
                    order_line_item.save()
                except Product.DoesNotExist:
                    messages.error(request, (
                        "One of the products in your basket doesn't exist in our database"
                        "Please contact us via the Contact us Page")
                    )
                    order.delete()
                    return redirect(reverse('view_basket'))
            
            request.session['save_info'] = 'save_info' in request.POST
            return redirect(reverse('checkout_success', args=[order, order_number]))
        else:
            messages.error(request, "There was an error in your form. \
                Please check all the information is correct!")
                 
    else:
        basket = request.session.get('basket', {})
        if not basket:
            messages.error(request, 'There is nothing in your basket!')
            return redirect(reverse('index'))

        current_basket = basket_contents(request)
        total = current_basket['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'You are missing your public key. \
            Please make sure it is set!')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    """
    Successful checkout view
    """

    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Your order was successfully processed! \
        Your order number is {order_number}. \
        A confirmation email is on the way to {order.email}. ')

    if 'basket' in request.session:
        del request.session['basket']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order
    }

    return render(request, template, context)
