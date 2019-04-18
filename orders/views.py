from django.views.generic import ListView, DetailView
from django.db.models import Q

from .models import Order


class AllOrdersListView(ListView):

    model = Order
    paginate_by = 10

    def get_queryset(self):
        search_val = self.request.GET.get('search', '')
        if search_val != '':
            try:
                updated_context = self.model.objects.filter(nb_items=search_val)\
                                                    .order_by('purchase_date')
            except ValueError:
                updated_context = self.model.objects.filter(
                    Q(unique_id__contains=search_val) | Q(marketplace__contains=search_val) |\
                    Q(billing_lastname__contains=search_val)
                ).order_by('purchase_date')

        else:
            updated_context = self.model.objects.all().order_by('purchase_date')
        return updated_context


class OrderDetailView(DetailView):

    model = Order
