
from django.urls import path
from .views import index, my_view, author_posts, post_full

urlpatterns = [
    path('', my_view, name='index'),
    path('author/<int:author_id>/', author_posts, name='author_posts'),
    path('post/<int:post_id>/', post_full, name='post_full'),



]

