from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Contact, Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list',)

class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

class ProductDetailView(DetailView):
    model = Product

class ContactListView(ListView):
    model = Contact

# def contact_list(request):
#     contacts = Contact.objects.all()
#     context = {'contacts': contacts}
#     if request.method == "POST":
#         name = request.POST.get('name')
#         contact = request.POST.get('phone')
#         message = request.POST.get('message')
#         print(f'Имя: {name}\nТелефон: {contact}\nСообщение: {message}\n')
#         Contact.objects.create(name=name, phone=contact, message=message)
#     return render(request, 'contact_list.html', context)


class ContactDetailView(ListView):
    model = Contact

class VersionListView(ListView):
    model = Version

class VersionCreateView(CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list',)

class VersionUpdateView(UpdateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list')

class VersionDeleteView(DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:version_list')

class VersionDetailView(DetailView):
    model = Version
