from django.shortcuts import render
from django.utils import timezone
from django.views.generic import ListView
from myapp3.models import Order, Product, User


# Create your views here.
def index(request):
    return render(request, "myapp3/index.html")

class OrderListView(ListView):
    model = Order
    template_name = "myapp3/order_list.html"
    context_object_name = 'orders'

class OrderProductListView(ListView):
    template_name = "myapp3/order_product_list.html"

    def get(self, request, pk, days=7):
        start_date = timezone.now() - timezone.timedelta(days=days)
        orders = Order.objects.filter(user_id=pk, order_date__gte=start_date).distinct()
        products = Product.objects.all()
        context = {'pk': pk, 'days': days, 'products': products, 'orders': orders}
        return render(request, self.template_name, context)
class AllOrderProductListView(ListView):
    template_name = "myapp3/all_order_product_list.html"
    def get(self, request):
        orders = Order.objects.all()
        products = Product.objects.all()
        context = {'products': products, 'orders': orders}
        return render(request, self.template_name, context)

