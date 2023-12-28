from django import forms

from catalog.models import Product, VersionProduct


class ProductForm(forms.ModelForm):
    exceptions = {'казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар'}

    class Meta:
        model = Product
        #fields = '__all__'
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        self.fields['version'].widget = forms.HiddenInput()
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data.get('product_name')
        data = [cleaned_data]
        if self.exceptions.intersection(set(data)):
            raise forms.ValidationError('нельзя: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.')

        return cleaned_data

    def clean_product_description(self):
        cleaned_data = self.cleaned_data.get('product_description')
        data = [cleaned_data]
        if self.exceptions.intersection(set(data)):
            raise forms.ValidationError('нельзя: казино, криптовалюта, крипта, биржа, дешево, бесплатно, обман, полиция, радар.')

        return cleaned_data


class Version(forms.ModelForm):
    class Meta:
        model = VersionProduct
        fields = '__all__'
