from django.db import models
from api.category.models import Category
   # Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    price = models.CharField(max_length=20)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True,blank=True)
    category = models.ForeignKey(Category, on_delete = models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    images = models.ImageField(blank=True,upload_to='images/',null=True)
    
    def __str__(self):
        return self.name

class SpareProduct(models.Model):
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=250)
    description  = models.CharField(max_length=500)
    stock = models.CharField(max_length=300)
    is_active = models.BooleanField(default = True, blank = True)