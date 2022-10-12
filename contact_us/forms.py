from django.forms import ModelForm
from django import forms
from .models import SignUp, ContactUs

class SignUpForm(ModelForm):
    """
    This form is connected with the Signup view
    so that visitors to the site can sign up
    for the shops newsletter.
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    email_address = forms.EmailField(
        label='Email Adress',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Adress'}),
    )


    class Meta:
        """Defines which model to pull the
        fields from"""
        model = SignUp
        # Tell the form to use all the fields provided
        fields = '__all__'


class ContactUsForm(ModelForm):
    """
    This form is connected with the contact_us view
    so that visitors to the site can contact the shop
    with their enquiries.
    It also provides the labels and placeholder
    text for each field, as wells as the widgets
    and handles validation where required.
    """

    first_name = forms.CharField(
        label='First Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'First Name'}),
    )

    last_name = forms.CharField(
        label='Last Name',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'}),
    )

    email_address = forms.EmailField(
        label='Email Adress',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Email Adress'}),
    )

    enquiry = forms.CharField(
        label='Enquiry',
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'How can we help?'}),
    )


    class Meta:
        """Defines which model to pull the
        fields from"""
        model = ContactUs
        # Tell the form to use all the fields provided
        fields = '__all__'