from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)# so that one user has only one
    #additional

    portfolio_site = models.URLField(blank=True)# user will decide whether he will provide
    # link or not.

    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)# to upload pictures to profile_pic
    # sub directory. blank = True because here user will decide whether to upload or not.


    def __str__(self):
        return self.user.username # username is default attribute of User.
