from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    """
    User Profile form to
    update user information
    """
    class Meta: 
        model = UserProfile()
        exclude = ('user',)


# Code taken from CI walkthrough project
    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'users_phone': 'Phone Number',
            'users_country': 'Country',
            'users_postcode': 'Postal Code',
            'users_town_or_city': 'Town or City',
            'users_street_address1': 'Street Address 1',
            'users_street_address2': 'Street Address 2',
            'users_county': 'County',
        }

        self.fields['users_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'user-profile-form'
            self.fields[field].label = False
