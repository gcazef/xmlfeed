from django.contrib import admin

from .models import Order


class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'marketplace',
        'purchase_date',
        'billing_lastname',
        'amount',
        'nb_items',
    )

    list_filter = (
        'amount',
        'nb_items',
    )

    search_fields = (
        'marketplace',
        'billing_lastname',
    )

admin.site.register(Order, OrderAdmin)
