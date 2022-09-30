from django.urls import path
from django.views.decorators.cache import cache_page
from .views import home_view, create_view, single_blog_view, update_view, delete, like_view, delete_likes

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('blogs/<int:id>', single_blog_view, name='single_blog'),
    path('update/<int:id>', update_view, name='update'),
    path('delete/<int:id>', delete, name="delete"),
    path('like/<int:pk>', like_view, name='like_post'),
    path('likedelete/', delete_likes, name='delete_likes')
]
