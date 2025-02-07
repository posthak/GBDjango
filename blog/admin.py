from django.contrib import admin
from .models import Author, Post


class AuthorAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['name', 'email']
    ordering = ['name']
    list_filter = ['email']
    search_fields = ['name']
    search_help_text = 'Поиск по полю name (name)'

class PostAdmin(admin.ModelAdmin):
    """Список продуктов."""
    list_display = ['title', 'content', 'author']
    ordering = ['author']
    list_filter = ['author']
    search_fields = ['content']
    search_help_text = 'Поиск по полю content (content)'


# Register your models here.
admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
