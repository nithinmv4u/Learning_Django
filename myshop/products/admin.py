from django.contrib import admin
from .models import Product,Offers,Sale

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')

class OfferAdmin(admin.ModelAdmin):
    list_display = ('code','description','discount')

class SaleAdmin(admin.ModelAdmin):
    list_display = ('name','num_sales')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Offers,OfferAdmin)
admin.site.register(Sale,SaleAdmin)
