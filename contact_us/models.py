from django.db import models
from django.contrib.auth.models import User

ENQUIRY_CHOICE = (
    ('Product', 'PRODUCT'),
    ('Pricing', 'PRICING'),
    ('Shipping', 'SHIPPING'),
    ('Returns', 'RETURNS'),
    ('General Enquiry', 'GENERAL ENQUIRY'),
)


class SignUp(models.Model):
    """
    Model to be used in the forms.py for the sign up to newsletter
    in the footer of each page a user goes onto.
    """

    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.first_name


class ContactUs(models.Model):
    """
    Model to be used in the forms.py for a contact form.
    There will be a link of this in the footer of each page.
    """

    first_name = models.CharField(max_length=60, null=True, blank=True)
    last_name = models.CharField(max_length=60, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    enquiry_type = models.CharField(
        max_length=50, choices=ENQUIRY_CHOICE, blank=False
    )
    enquiry = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.first_name
