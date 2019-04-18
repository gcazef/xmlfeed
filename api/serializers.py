from rest_framework import serializers

from orders import models


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        fields = (
            'id',
            'unique_id',
            'marketplace',
            'purchase_date',
            'billing_lastname',
            'amount',
            'nb_items',
        )
        model = models.Order
