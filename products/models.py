from django.db import models
from django.contrib.auth.models import User

# The choices for the status of reviews
STATUS = ((0, "Waiting Approval"), (1, "Approved"))


class Category(models.Model):
    """
    The model used for displaying
    the categories
    """

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    """
    The model used for displaying
    the products
    """
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    """
    Allows authorised users to
    add reviews for products on
    the site
    """
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_title = models.CharField(max_length=150)
    content = models.TextField()
    created = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=1)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.review_title
