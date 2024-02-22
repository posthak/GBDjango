
from django.urls import path
from .views import OrderListView, OrderProductListView, \
    index, add_product, ViewProduct, ViewUser, add_update_product

urlpatterns = [
    path('', index, name='index'),
    path('orders/', OrderListView.as_view(), name='order_list'),
    path('products/<int:pk>/<int:days>', OrderProductListView.as_view(), name='user_products'),
    path('products/', ViewProduct.as_view(), name='view_products'),
    path('users/', ViewUser.as_view(), name='view_users'),
    path('product/add', add_update_product, name='add_product'),
    path('product/update', add_update_product, name='update_product_page'),
    path('product/update/<int:pk>', add_update_product, name='update_product'),

]

