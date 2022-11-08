from django import forms
from .models import Product, Category, Review


class ManageProductsForm(forms.ModelForm):
    """
    The form allows the store
    owner to add/update/delete products
    without login to the admin site
    """

    class Meta:
        model = Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'user-profile-form'


class ReviewForm(forms.ModelForm):
    """
    The form that allows login
    users to add reviews for
    products on the site
    """

    class Meta:
        model = Review
        fields = ('review_title', 'product', 'content',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'review_title': 'Title',
            'product': 'Product',
            'content': 'Review',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'modal-elements'
            self.fields[field].label = False


