from django import forms
from django.contrib.auth.models import User
from basicusers_app.models import UserProfileInfo


class UserForm(forms.ModelForm):# if we use model form then it will automatically store in database.
    password= forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')# these are fields defined by django automatically
        # and this is all we require .


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')
