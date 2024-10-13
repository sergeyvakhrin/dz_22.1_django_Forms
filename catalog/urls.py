from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, ProductDetailView, ContactDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView, VersionListView, VersionDetailView, VersionCreateView, VersionUpdateView, VersionDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('products/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='contact_detail'),
    path('products/create', ProductCreateView.as_view(), name="product_create"),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),

    path('version/', VersionListView.as_view(), name='version_list'),
    path('version/<int:pk>', VersionDetailView.as_view(), name='version_detail'),
    path('version/create', VersionCreateView.as_view(), name="version_create"),
    path('version/<int:pk>/update/', VersionUpdateView.as_view(), name="version_update"),
    path('version/<int:pk>/delete/', VersionDeleteView.as_view(), name="version_delete"),
]