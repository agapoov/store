from django.urls import path

from orders.views import (CanceledTemplateView, OrderCreateView,
                          OrderDetailView, OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order_create/', OrderCreateView.as_view(), name='order_create'),
    path('', OrderListView.as_view(), name='orders_list'),
    path('order-success/', SuccessTemplateView.as_view(), name='order-success'),
    path('order-cancel/', CanceledTemplateView.as_view(), name='order-cancel'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),

]
