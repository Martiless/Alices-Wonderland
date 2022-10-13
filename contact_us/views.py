from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import FormView
from .forms import SignUpForm, ContactUsForm


class SignUpView(FormView):
    """
    Renders the Sign up form page in the browser
    Using the SignUpForm created in the forms.py file
    When the Sign up form is completed and submitted
    the user will receive a message to say it was
    successful.
    """
    template_name = 'sign_up.html'
    form_class = SignUpForm

    def sign_up_view(self, request):
        return render(request, 'sign_up.html')

    def post(self, request):
        """
        Uses the SignUpForm from forms.py
        Checks if all the infromation in valid
        and then saves it to the database.
        Once the information is saved the site
        visitor will receive a pop up message
        """
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            form.save()
        # Pops up a message to the site visitor when their information
        # has been saved
        messages.success(request, 'Thank you for signing up to our newsletter')
        return redirect('/')


class ContactUsView(FormView):
    """
    Renders the Contact form page in the browser
    Using the ContactUsForm created in the forms.py file
    When the Contact form is completed and submitted
    the user will receive a message to say it was
    successful.
    """
    template_name = 'contact_us.html'
    form_class = ContactUsForm

    def contact_us_view(self, request):
        return render(request, 'contact_us.html')

    def post(self, request):
        """
        Uses the ContactUsForm from forms.py
        Checks if all the infromation in valid
        and then saves it to the database.
        Once the information is saved the site
        visitor will receive a pop up message
        """
        form = ContactUsForm(data=request.POST)
        if form.is_valid():
            form.save()
        # Pops up a message to the site visitor when their information
        # has been saved
        messages.success(request, 'Thank you for contacting us. We will get back to your enquiry as soon as possible')
        return redirect('/')
