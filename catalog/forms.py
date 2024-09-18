from django.forms import ModelForm, forms

from catalog.models import Product, Version


class ProductForm(ModelForm):

    words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        for word in self.words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое название использовать нельзя')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        for word in self.words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое описание использовать нельзя')
        return cleaned_data


class VersionForm(ModelForm):

    class Meta:
        model = Version
        fields = "__all__"