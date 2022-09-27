from django.urls import path
from .views import home_view, create_view, single_blog_view, update_view, delete

urlpatterns = [
    path('', home_view, name='home'),
    path('create/', create_view, name='create'),
    path('blogs/<int:id>', single_blog_view, name='single_blog'),
    path('update/<int:id>', update_view, name='update'),
    path('delete/<int:id>', delete, name="delete"),

]