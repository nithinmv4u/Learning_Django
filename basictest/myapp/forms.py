from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product', 'make', 'price', 'stock', 'description', 'product_image']
        exclude = ['is_enabled', 'created_date', 'modified_date']