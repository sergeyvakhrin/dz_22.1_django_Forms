from django.forms import ModelForm, forms

from catalog.models import Product, Version

words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class ProductForm(ModelForm):

    class Meta:
        model = Product
        fields = "__all__"

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name'] #TODO: реализовать метод, что бы избежать дублирования кода
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое название использовать нельзя')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description'] #TODO: реализовать метод, что бы избежать дублирования кода
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое описание использовать нельзя')
        return cleaned_data


class VersionForm(ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['name'] #TODO: реализовать метод, что бы избежать дублирования кода
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое наименование использовать нельзя')
        return cleaned_data


    def clean_number_version(self):
        cleaned_data = self.cleaned_data['number_version'] #TODO: реализовать метод, что бы избежать дублирования кода
        for word in words:
            if word in cleaned_data:
                raise forms.ValidationError('Такое наименование использовать нельзя')
        return cleaned_data

