from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm, ContactUsForm


def get_sign_up_form(request):
    """
    Renders the Sign up form page in the browser
    Using the SignUpForm created in the forms.py file
    When the Sign up form is completed and submitted
    the user will receive a message to say it was
    successful.
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignUpForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Thank you for signing up to our Newsletter!')
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignUpForm()

    return render(request, 'contact_us/sign_up.html', {'form': form})


def get_contact_us_form(request):
    """
    Renders the Sign up form page in the browser
    Using the SignUpForm created in the forms.py file
    When the Sign up form is completed and submitted
    the user will receive a message to say it was
    successful.
    """
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactUsForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            messages.success(request, 'Thank you for contacting us. We will get back to you as soon as possible!')
            return HttpResponseRedirect('/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactUsForm()

    return render(request, 'contact_us/contact_us.html', {'form': form})
