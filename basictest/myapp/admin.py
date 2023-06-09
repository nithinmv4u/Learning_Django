from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=('product', 'make', 'price', 'stock', 'description', 'product_image')

admin.site.register(Product, ProductAdmin)