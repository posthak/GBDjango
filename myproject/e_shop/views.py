from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from .forms import ProductForm
from e_shop.models import Order, Product, User


# Create your views here.
def index(request):
    return render(request, "e_shop/index.html")

class OrderListView(ListView):
    model = Order
    template_name = "e_shop/order_list.html"
    context_object_name = 'orders'

class OrderProductListView(ListView):
    template_name = "e_shop/order_product_list.html"

    def get(self, request, pk, days=7):
        start_date = timezone.now() - timezone.timedelta(days=days)
        orders = Order.objects.filter(user_id=pk, order_date__gte=start_date).distinct()
        products = Product.objects.all()
        context = {'pk': pk, 'days': days, 'products': products, 'orders': orders}
        return render(request, self.template_name, context)

class ViewProduct(ListView):
    template_name = "e_shop/view_products.html"
    model = Product
    context_object_name = 'products'

class ViewUser(ListView):
    template_name = "e_shop/view_user.html"
    model = User
    context_object_name = 'users'

def add_product(request):
    template_name = "e_shop/add_product.html"
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm()

    return render(request, template_name, {'form': form})

def add_update_product(request, pk=None):
    template_name = "e_shop/add_update_product.html"
    if pk:
        product = get_object_or_404(Product, pk=pk)
        action = 'Update'
    else:
        product = None
        action = 'Add'

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('view_products')
    else:
        form = ProductForm(instance=product)
    return render(request, template_name, {'form': form, 'action': action})
