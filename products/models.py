# ./products/models.py

from django.db import models
from django.utils import timezone

class Product(models.Model):
    
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places = 2, max_digits = 10)
    sku = models.CharField(max_length=10)
    category = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    image = models.ImageField(
        blank = True, null = True,
        upload_to = 'media/products'
        )
    
    discount = models.IntegerField()
    
    create_date = models.DateTimeField(
        default = timezone.now)
    publish_date = models.DateTimeField(
        blank = True, null = True)
    