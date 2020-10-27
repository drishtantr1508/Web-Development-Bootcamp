from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=40)
    lastname = models.CharField(max_length=40)
    contact= models.PositiveIntegerField()

    def __str__(self):
        return self.firstname+self.lastname
