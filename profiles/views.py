from django.shortcuts import render


def user_profile(request):
    """
    The view to display
    the user's profile
    """
    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)

