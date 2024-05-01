from django import forms
from django.forms import BooleanField
from django.views.generic import CreateView

from catalog.models import Product, Version


class StyleMixin():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(forms.ModelForm):
    BAD_WORDS = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in cleaned_data.split():
            if word in self.BAD_WORDS:
                raise forms.ValidationError('Так нельзя! Придумай другое имя.')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in cleaned_data.split():
            if word in self.BAD_WORDS:
                raise forms.ValidationError('Так нельзя! Убери плохие слова!')
        return cleaned_data


class VersionForm(forms.ModelForm, StyleMixin):

    class Meta:
        model = Version
        fields = '__all__'
