from django.contrib import admin
from .models import Order, Product, User, Category

@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class UserAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'email', 'mob_number']
    ordering = ['name', '-mob_number']
    list_filter = ['date_reg', 'mob_number']
    search_fields = ['address']
    search_help_text = 'Поиск по полю address (address)'
    actions = [reset_quantity]

class ProductAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'category', 'quantity']
    ordering = ['category', '-quantity']
    list_filter = ['date_created', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'
    actions = [reset_quantity]

    readonly_fields = ['date_created']
    fieldsets = [
                (
                    None,
                    {
                        'classes': ['wide'],
                        'fields': ['name'],
                    },
                ),
                (
                    'Детали',
                    {
                        'classes': ['collapse'],
                        'description': 'Категория товара и его подробное описание',
                        'fields': ['category', 'description'],
                    },
                ),
                (
                    'Финансы',
                    {
                        'fields': ['price', 'quantity'],
                    }
                ),
                (
                    'Прочее',
                    {
                        'fields': ['photo', 'date_created'],
                    }
                ),
    ]

class OrderAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['id', 'order_date', 'total_price']
    ordering = ['-total_price']
    list_filter = ['order_date', 'total_price']

class CategoryAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['id', 'name']
    ordering = ['-name']
    list_filter = ['id', 'name']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name (name)'


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

