from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfileInfo(models.Model):

    user= models.OneToOneField(User,on_delete=models.CASCADE)# to create a relationship instead of inheriting like models.UserProfileInfo

    # this user attribute contains all the necessary fields like username,paswords,email,

    # firstname and lastname. But if you want to have additional fields like for profile pic etc

    # you can always have it.

    #additional fields

    portfolio_site = models.URLField(blank=True)

    profile_pic=models.ImageField(blank=True, upload_to='profile_pic')#where prfile_pic is a folder
    #in media folder to store profile pictures.

    def __str__(self):
        return self.user.username# remember user is set of fields created automatically using Django's
        # built in User. We are returning username field from that set.
