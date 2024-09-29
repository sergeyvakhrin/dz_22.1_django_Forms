from django.forms import ModelForm, forms, BooleanField

from catalog.models import Product, Version
from config.settings import forbidden_words


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'



class ProductForm(StyleMixin, ModelForm):

    class Meta:
        model = Product
        # fields = "__all__"
        exclude = ("owner",)

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']
        validate_clean(cleaned_data, 'Такое название использовать нельзя')
        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data['product_description']
        validate_clean(cleaned_data,'Такое описание использовать нельзя')
        return cleaned_data


class VersionForm(StyleMixin, ModelForm):

    class Meta:
        model = Version
        fields = "__all__"

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        validate_clean(cleaned_data,'Такое наименование использовать нельзя')
        return cleaned_data


    def clean_number_version(self):
        cleaned_data = self.cleaned_data['number_version']
        validate_clean(cleaned_data, 'Такой номер использовать нельзя')
        return cleaned_data


def validate_clean(cleaned_data, validation_error: str) -> None:
    """
    Функция для проверки и генерации ошибки
    """
    for word in forbidden_words:
        if word in cleaned_data:
            raise forms.ValidationError(validation_error)