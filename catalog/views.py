from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm
from catalog.models import Contact, Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.models import User


class ProductListView(ListView, LoginRequiredMixin):
    model = Product

    # def get_queryset(self):
    #     """ Фильтрация продуктов по наличию активной версии """
    #
    #     data = super().get_queryset().filter(versions=True)
    #
    #     return data


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list',)

    def form_valid(self, form):
        # product = form.save()
        # product.owner = self.request.user
        # product.save()
        form.instance.owner = self.request.user # так исключается одно обращение к базе

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        ProductFormset = inlineformset_factory(Product, Version, VersionForm, extra=1)
        if self.request.method == "POST":
            context_data['formset'] = ProductFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = ProductFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        if form.is_valid() and formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()
            return super().form_valid(form)
        else:
            return self.render_to_response(self.get_context_data(form=form, formset=formset))


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

class ProductDetailView(DetailView):
    model = Product

################# Contact ##################

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

######################## Version #################

class VersionListView(LoginRequiredMixin, ListView):
    model = Version

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        return context_data


class VersionCreateView(LoginRequiredMixin, CreateView):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list',)

class VersionUpdateView(UpdateView, LoginRequiredMixin):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list')

class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:version_list')

class VersionDetailView(DetailView, LoginRequiredMixin):
    model = Version
