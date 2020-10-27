from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Company(models.Model):
    name=models.CharField(max_length=100)
    ceo=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("cbv_app:companylist")
class Employee(models.Model):
    name=models.CharField(max_length=100)
    age=models.PositiveIntegerField()
    company=models.ForeignKey(Company,related_name='employees' , on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("cbv_app:companylist")


class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    # Additional Stuff
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    experience=models.PositiveIntegerField()
    portfolio_site=models.URLField()
    profile_pic=models.ImageField(blank=True)

    def __str__(self):
        return self.user.username
