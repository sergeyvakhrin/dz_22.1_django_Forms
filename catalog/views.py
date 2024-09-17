from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.models import Contact, Product
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class ProductListView(ListView):
    model = Product

class ProductCreateView(CreateView):
    model = Product
    fields = ("product_name", "product_description", "product_image", "category", "price",)
    success_url = reverse_lazy('catalog:product_list',)

class ProductUpdateView(UpdateView):
    model = Product
    fields = ("product_name", "product_description", "product_image", "category", "price")
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


class ContactDetailView(DetailView):
    model = Contact

