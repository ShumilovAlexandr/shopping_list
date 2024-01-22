from django import forms

from .models import Product


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'image', 'description', 'price', 'quantity']
        widgets = {
            'name': forms.TextInput(
                attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control'}),
            'description': forms.Textarea(
                attrs={'cols': 50, 'rows': 5,
                       'class': 'form-control'}),
            'price': forms.NumberInput(
                attrs={'class': 'form-control'}),
            'quantity':  forms.NumberInput(
                attrs={'class': 'form-control'}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(AddProductForm, self).__init__()
    #     for field_name in self.fields:
    #         self.fields[field_name].label = ''
