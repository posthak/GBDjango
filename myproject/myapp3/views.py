from django.shortcuts import render
from django.utils import timezone
from django.views import View
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
    model = Product
    template_name = "myapp3/order_product_list.html"
    context_object_name = 'products'


    def get_queryset(self):
        # Получаем параметр N из URL (если передан)
        days = self.request.GET.get('days', None)
        print(days)

        # Устанавливаем значение по умолчанию (например, 7 дней, если не передано другое)
        if not days:
            days = 7

        # Вычисляем начальную дату (сегодня - N дней)
        start_date = timezone.now() - timezone.timedelta(days=int(days))
        # Фильтруем товары, связанные с заказами, созданными в указанный временной диапазон
        queryset = Product.objects.filter(order__order_date__range=(start_date, timezone.now())).distinct()
        print(queryset)
        return queryset

