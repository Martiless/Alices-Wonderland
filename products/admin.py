from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    """This adds the product display list
    to the database in the admin site"""

    list_display = (
        'name',
        'category',
        'sku',
        'price',
        'rating',
        'image'
    )

    ordering = ('sku', 'name', 'rating',)


class CategoryAdmin(admin.ModelAdmin):
    """This adds the category display list
    to the database in the admin site"""

    list_display = (
        'name',
        'friendly_name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
