from django.contrib import admin
from .models import Order, OrderLineItems


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Used to add or adjust order items
    if needed in the admin site
    """
    model = OrderLineItems
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    """
    This displays the Orders in the
    database in the admin site
    """
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                        'shipping_cost', 'order_total',
                        'grand_total',)

    fields = ('order_number', 'user_profile', 'date', 'full_name',
              'email_address', 'phone', 'country',
              'postcode', 'town_or_city', 'street_address1',
              'street_address2', 'county', 'shipping_cost',
              'order_total', 'grand_total',)

    list_display = ('order_number', 'date', 'full_name',
                    'email_address', 'order_total',
                    'shipping_cost', 'grand_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)
