from django.contrib import admin

from catalog.models import Product, Category, Contact
from blog.models import Blog


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'price', 'category', 'created_at', 'updated_at',)
    list_filter = ('category_id',)
    search_fields = ('product_name', 'product_description',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category_name',)
    list_filter = ('category_name',)
    search_fields = ('category_name', 'category_description',)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'message',)
    list_filter = ('name', 'phone',)
    search_fields = ('name', 'phone', 'message',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'post', 'slug', 'created_at', 'is_published', 'views_count')
    list_filter = ('is_published',)
    search_fields = ('title', 'post',)