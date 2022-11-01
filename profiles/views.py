from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm



def user_profile(request):
    """
    The view to display
    the user's profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save
            messages.success(request, 'Your profile has been successfully updated!')

    form = UserProfileForm(instance=profile)
    order = profile.orders.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'order': order,
    }

    return render(request, template, context)
