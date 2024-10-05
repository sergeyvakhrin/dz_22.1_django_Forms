from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.forms import inlineformset_factory
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse_lazy

from catalog.forms import ProductForm, VersionForm, ProductModeratorsForm
from catalog.models import Contact, Product, Version
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from users.models import User


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Product
    permission_required = ['catalog.view_product']

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = ['catalog.add_product']
    success_url = reverse_lazy('catalog:product_list',)

    def form_valid(self, form):
        # product = form.save()
        # product.owner = self.request.user
        # product.save()
        form.instance.owner = self.request.user # так исключается одно обращение к базе

        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = ['catalog.change_product']
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

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return ProductForm
        if user.has_perm('catalog.can_edit_published') and user.has_perm('catalog.can_edit_product_description') and user.has_perm('catalog.can_edit_category_product'):
            return ProductModeratorsForm
        raise PermissionDenied


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')

    def test_func(self):
        return self.request.is_superuser


class ProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Product
    permission_required = ['catalog.view_product']

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        if self.request.user == self.object.owner:
            return self.object
        raise PermissionDenied


################# Contact ##################

class ContactListView(LoginRequiredMixin, ListView):
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


class ContactDetailView(LoginRequiredMixin, ListView):
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

class VersionUpdateView(LoginRequiredMixin, UpdateView,):
    model = Version
    form_class = VersionForm
    success_url = reverse_lazy('catalog:version_list')

class VersionDeleteView(LoginRequiredMixin, DeleteView):
    model = Version
    success_url = reverse_lazy('catalog:version_list')

class VersionDetailView(LoginRequiredMixin, DetailView):
    model = Version
