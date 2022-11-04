from django.contrib import admin
from .models import Product, Category, Review


class ProductAdmin(admin.ModelAdmin):
    """
    This adds the product display list
    to the database in the admin site
    """

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
    """
    This adds the category display list
    to the database in the admin site
    """

    list_display = (
        'name',
        'friendly_name'
    )


class ReviewsAdmin(admin.ModelAdmin):
    """
    This adds the reviews display list
    to the database in the admin site
    """

    list_display = (
        'reviewer',
        'review_title',
        'created',
        'status'
    )

    ordering = ('reviewer', 'created', 'status',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewsAdmin)
