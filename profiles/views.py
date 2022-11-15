from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def user_profile(request):
    """
    The view to display
    the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been \
                successfully updated!')
        else:
            messages.error(request, 'Your profile failed to update.\
                Please check the form and try again!')
    else:
        form = UserProfileForm(instance=profile)

    order = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': order,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    The view to generate the users
    order history when on their profile
    page
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a confirmation for order number {order_number}.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
