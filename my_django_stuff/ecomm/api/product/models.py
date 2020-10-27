from django.db import models
from api.category.models import Category

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.CharField(max_length=15)
    stock = models.CharField(max_length=50)
    is_active = models.BooleanField(blank = True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True,null=True, upload_to='images/')

    def __str__(self):
        return self.name