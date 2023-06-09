from django.contrib import admin
from .models import MyModel

# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display=('id','my_field','my_num')

admin.site.register(MyModel,MyModelAdmin)