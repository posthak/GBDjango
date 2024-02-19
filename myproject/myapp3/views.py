from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView
from .forms import ProductForm
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

class ViewProduct(ListView):
    template_name = "myapp3/view_products.html"
    model = Product
    context_object_name = 'products'

def add_product(request):
    template_name = "myapp3/add_product.html"
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()

    return render(request, template_name, {'form': form})
