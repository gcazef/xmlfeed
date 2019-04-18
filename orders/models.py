from django.db import models


class Order(models.Model):

    unique_id = models.CharField(null=False, unique=True, max_length=25)
    marketplace = models.CharField(null=False, max_length=50)
    purchase_date = models.DateField(null=True)
    billing_lastname = models.CharField(null=True, max_length=200)
    amount = models.FloatField(null=False)
    nb_items = models.IntegerField(null=False)
