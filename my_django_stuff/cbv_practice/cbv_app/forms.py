from django import forms
from .models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control',
                                'placeholder':'Enter your Password Here'
                }))

    class Meta():
        model=User
        fields=('username','email','password')
        widgets={
            'username': forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter your username here... '
            }),
            'email': forms.EmailInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter your Email here... '
            })
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('firstname','lastname','experience','portfolio_site','profile_pic')
        widgets={
            'firstname': forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter your First name here... '
            }),
            'lastname': forms.TextInput(attrs={
                    'class':'form-control',
                    'placeholder':'Enter your Last name here... '
            }),
            'experience':forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'How much experience do you have... ?',

            }),
            'portfolio_site':forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'Enter you Website here...',

            }),

        }
