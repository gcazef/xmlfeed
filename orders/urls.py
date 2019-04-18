from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllOrdersListView.as_view(), name='allorders'),
    path('order/<int:pk>', views.OrderDetailView.as_view(), name='order')
]
