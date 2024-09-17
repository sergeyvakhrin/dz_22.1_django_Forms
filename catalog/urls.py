from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactListView, ProductDetailView, ContactDetailView, ProductCreateView, \
    ProductUpdateView, ProductDeleteView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('contacts/', ContactListView.as_view(), name='contacts'),
    path('products/<int:pk>', ProductDetailView.as_view(), name='product_detail'),
    path('contacts/<int:pk>', ContactDetailView.as_view(), name='contact_detail'),
    path('products/create', ProductCreateView.as_view(), name="product_create"),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name="product_update"),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name="product_delete"),
]