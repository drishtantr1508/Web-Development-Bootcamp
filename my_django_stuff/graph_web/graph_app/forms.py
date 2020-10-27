from django import forms
from django.contrib.auth.models import User
from graph_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password = forms.CharField(widgets=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta():
        model = User
        fields = ('username','email','password')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your username here...'}),
            'email'  : forms.TextInput(attrs={'class':'form-control','placeholder':'example@gmail.com'})

        }

class UserProfileInfoForm(forms.ModelFrom):
    class Meta():
        model = UserProfileInfo
        fields = "__all__"
        widgets= {
            'firstname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter
            your first name...'}),
            'lastname':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter
             your last name...'}),
            'contact':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter
                 your Contact No...'}),
        }
