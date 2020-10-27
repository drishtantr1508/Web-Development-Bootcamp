from django.db import models

# Create your models here
class User(models.Model):
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    def __str__(self):
        return self.first_name+self.last_name

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.CharField(max_length=150)
    def __str__(self):
        return self.address
