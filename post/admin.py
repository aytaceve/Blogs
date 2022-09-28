from django.contrib import admin
from .models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    fields = ['user', 'title', 'content','created_at', 'likes']
    readonly_fields = ('created_at',)

admin.site.register(Blog, BlogAdmin)