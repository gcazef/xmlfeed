from django.test import TestCase

from orders import models


class OrderTest(TestCase):

    def setUp(self):
        super().setUp()
        self.order = models.Order.objects.create(unique_id='12345', marketplace='azamon',
                                                amount='41.99', nb_items='3')

    def test_order_created(self):
        db_count = models.Order.objects.all().count()
        db_order = models.Order.objects.last()
        self.assertEqual(db_count, 1)
        self.assertEqual(self.order, db_order)
        self.assertEqual(db_order.unique_id, self.order.unique_id)
        self.assertTrue(isinstance(db_order, models.Order))
