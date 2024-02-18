
from django.urls import path
from .views import OrderListView, OrderProductListView, index, AllOrderProductListView

urlpatterns = [
    path('', index, name='index'),
    path('orders', OrderListView.as_view(), name='order_list'),
    path('products/', AllOrderProductListView.as_view(), name='all_order_product_list'),
    path('products/<int:pk>/<int:days>/', OrderProductListView.as_view(), name='user_products'),
]

