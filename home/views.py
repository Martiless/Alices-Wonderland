from django.shortcuts import render

# Create your views here.

def index(request):
    """
    Renders the home page
    """

    return render(request, 'home/index.html')

def about_me(request):
    """
    Renders the about me page
    """

    return render(request, 'home/about_me.html')

def privacy_policy(request):
    """
    Renders the privacy policy page
    """

    return render(request, 'home/privacy_policy.html')
