from django.urls import path
from .views import home_view, create_view, single_blog_view, update_view, delete, like_view, delete_likes, login_view, logout_view, register_view

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('blogs/<int:id>', single_blog_view, name='single_blog'),
    path('update/<int:id>', update_view, name='update'),
    path('delete/<int:id>', delete, name="delete"),
    path('like/<int:pk>', like_view, name='like_post'),
    path('likedelete/', delete_likes, name='delete_likes'),
]
