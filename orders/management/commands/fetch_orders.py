import lxml.etree as etree

from django.core.management.base import BaseCommand
from django.conf import settings
from datetime import datetime

from orders.models import Order


class Command(BaseCommand):
    """ This command parses XML from the Lengow test API and
        saves it in the an Order Model instance.

        To add a field, modify the model and the 'fields' attribute
        of this class, following the pattern:
        (field_name, field_type, xml_field_path)
    """

    help = 'Fetch new orders from API'
    root = etree.parse(settings.ORDER_API_URL).getroot()
    fields = (
        ('unique_id', str, '/order_id'),
        ('marketplace', str, '/marketplace'),
        ('purchase_date', datetime.date, '/order_purchase_date'),
        ('billing_lastname', str, '/billing_address/billing_lastname'),
        ('amount', float, '/order_amount'),
        ('nb_items', int, '/order_items')
    )

    def str_to_date(self, str_date):
        try:
            date = datetime.strptime(str_date, ("%Y-%m-%d"))
        except ValueError:
            date = None
        return date

    def get_value(self, path, field_type, pos):
        str_value = self.root.xpath('//order' + path)[pos].text
        if field_type == datetime.date:
            return self.str_to_date(str_value)
        else:
            return field_type(str_value)

    def handle(self, *args, **kwargs):
        nb_orders = int(self.root.xpath('//statistics/orders_count/count_total')[0].text)
        for i in range(nb_orders):
            new_order = Order()
            for name, field_type, path in self.fields:
                setattr(new_order, name, self.get_value(path, field_type, i))
            new_order.save()
