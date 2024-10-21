from django import forms

from .models import Product

class prductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'title',
            'description',
            'price',
            'color',
        ]