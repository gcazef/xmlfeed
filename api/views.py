from rest_framework import viewsets

from orders import models
from . import serializers


class OrderViewSet(viewsets.ModelViewSet):

    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
