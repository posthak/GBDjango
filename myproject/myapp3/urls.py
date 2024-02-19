
from django.urls import path
from .views import OrderListView, OrderProductListView, index, add_product, ViewProduct

urlpatterns = [
    path('', index, name='index'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('products/<int:pk>/<int:days>/', OrderProductListView.as_view(), name='user_products'),
    path('add_product/', add_product, name='add_product'),
    path('products/', ViewProduct.as_view(), name='view_products'),
]

