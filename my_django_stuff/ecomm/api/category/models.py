from django.db import models

# Create your models here.


class Category(models.Model):
    
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    seasons = models.CharField(max_length=30,blank=True)
    materials = models.CharField(max_length=30,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):#this is used to see the object as their name it will return category.name in admin page
        return self.name
