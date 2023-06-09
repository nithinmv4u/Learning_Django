from django.db import models
from django.utils import timezone

# Create your models here.
class Product(models.Model):
    MAKE_CHOICES = [
        ('BATA', 'Bata'),
        ('ADIDAS', 'Adidas'),
        ('PUMA', 'Puma'),
        ('REEBOK', 'Reebok'),
        ('NIKE', 'Nike'),
        ('WOODLAND', 'Woodland'),
        ('RED_CHIEF', 'Red Chief'),
        ('LEE_COOPER', 'Lee Cooper'),
        ('FILA', 'Fila'),
        ('SKECHERS', 'Skechers'),
        ('CONVERSE', 'Converse'),
        ('CLARKS', 'Clarks'),
        ('CROCS', 'Crocs'),
        ('HUSH_PUPPIES', 'Hush Puppies'),
        ('LIBERTY', 'Liberty'),
        ('SPARX', 'Sparx'),
        ('ACTION', 'Action'),
        ('LANCER', 'Lancer'),
        ('LOTTO', 'Lotto'),
        ('MOCHI', 'Mochi'),
    ]

    product = models.CharField(max_length=255)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    make = models.CharField(max_length=255, choices=MAKE_CHOICES,)
    price = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)
    description = models.TextField(default='', blank=True)
    product_image = models.ImageField(upload_to='products', null=True, blank=True)
    is_enabled = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(auto_now=True)