from django import forms
from .models import Product, Category


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
        super().__init__(*args, *kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'user-profile-form'