
from django.urls import path
from .views import OrderListView, OrderProductListView, index

urlpatterns = [
    path('', index, name='index'),
    path('orders', OrderListView.as_view(), name='order_list'),
    path('products/', OrderProductListView.as_view(), name='order_product_list'),
]

