from django.contrib import admin
from .models import SignUp, ContactUs


class SignUpAdmin(admin.ModelAdmin):
    """This adds the Sign up list
    to the database in the admin site"""
    
    list_display = (
        'first_name',
        'last_name',
        'email_address'
    )




class ContactUsAdmin(admin.ModelAdmin):
    """This adds the Contact us display list
    to the database in the admin site"""

    list_display = (
        'first_name',
        'last_name',
        'email_address',
        'enquiry_type',
        'enquiry'
    )


admin.site.register(SignUp, SignUpAdmin)
admin.site.register(ContactUs, ContactUsAdmin)
