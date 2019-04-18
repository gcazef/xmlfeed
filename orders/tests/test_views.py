from django.http import HttpRequest
from django.test import TestCase
from django.urls import reverse

from orders import models


class MainPageTest(TestCase):

    def _create_orders(self):
        models.Order.objects.create(unique_id='12345', marketplace='azamon',
                                    amount='41.99', nb_items='3')
        models.Order.objects.create(unique_id='54321', marketplace='ddiscount',
                                    amount='0.99', nb_items='1')

    def test_main_status_code(self):
        with self.assertNumQueries(1):
            response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_bad_request(self):
        with self.assertNumQueries(0):
            response = self.client.get('/azerty/')
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        with self.assertNumQueries(1):
            response = self.client.get(reverse('allorders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'orders/order_list.html')

    def test_empty_database(self):
        with self.assertNumQueries(1):
            response = self.client.get(reverse('allorders'))
        self.assertNotContains(response, '<div class="card">')

    def test_contains_orders(self):
        self._create_orders()
        with self.assertNumQueries(2):
            response = self.client.get(reverse('allorders'))
        self.assertContains(response, '<div class="card">')
        self.assertContains(response, '12345')
        self.assertContains(response, '54321')
        self.assertEqual(response.status_code, 200)

    def test_main_page_search_success(self):
        self._create_orders()        
        with self.assertNumQueries(2):
            response = self.client.get('/', {'search': 'azamon'})
        self.assertContains(response, '<div class="card">')
        self.assertContains(response, '12345')
        self.assertNotContains(response, '54321')
        self.assertEqual(response.status_code, 200)

    def test_main_page_search_fail(self):
        self._create_orders()        
        with self.assertNumQueries(1):
            response = self.client.get('/', {'search': 'qwerty'})
        self.assertNotContains(response, '<div class="card">')
        self.assertNotContains(response, '12345')
        self.assertNotContains(response, '54321')
        self.assertEqual(response.status_code, 200)


class DetailsPageTest(TestCase):

    def _create_orders(self):
        self.order_1 = models.Order.objects.create(unique_id='12345', marketplace='azamon',
                                    amount='41.99', nb_items='3')
        self.order_2 = models.Order.objects.create(unique_id='54321', marketplace='ddiscount',
                                    amount='0.99', nb_items='1')

    def test_main_status_code(self):
        self._create_orders()
        with self.assertNumQueries(1):
            response = self.client.get(reverse('order', args=[self.order_1.id]))
        self.assertContains(response, self.order_1.unique_id)
        self.assertEqual(response.status_code, 200)
        with self.assertNumQueries(1):
            response = self.client.get(reverse('order', args=[self.order_2.id]))
        self.assertContains(response, self.order_2.unique_id)        
        self.assertEqual(response.status_code, 200)

    def test_bad_request(self):
        self._create_orders()
        with self.assertNumQueries(1):
            response = self.client.get(reverse('order', args=[12345]))
        self.assertEqual(response.status_code, 404)

    def test_no_order(self):
        with self.assertNumQueries(1):
            response = self.client.get(reverse('order', args=[1]))
        self.assertEqual(response.status_code, 404)

    def test_view_uses_correct_template(self):
        self._create_orders()
        with self.assertNumQueries(1):
            response = self.client.get(reverse('order', args=[self.order_1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'orders/order_detail.html')
