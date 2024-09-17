from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogListView.as_view(), name='blog_list'),
    path('<slug>/view/', BlogDetailView.as_view(), name='blog_detail'),
    path('create/', BlogCreateView.as_view(), name="blog_create"),
    path('<slug>/update/', BlogUpdateView.as_view(), name="blog_update"),
    path('<slug>/delete/', BlogDeleteView.as_view(), name="blog_delete"),
]