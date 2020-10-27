from django import forms
from django.contrib.auth.models import User
from auth_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(attrs={
                        'class':'form-control',
                        'placeholder':'Enter you Password here...',
    # we always define fieds ourselves for which we have to modifiication like this .In views we will set it as
    # password for the user and like anyother field named password.
    }))

    class Meta():
        model= User
        fields=("username","email","password")
        widgets={
            'username':forms.TextInput(attrs={
                                'class':'form-control',
                                'placeholder':'Enter you username here...',

            }),
            'email':forms.EmailInput(attrs={
                                'class':'form-control',
                                'placeholder':'Enter you Email here...',

            })
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model=UserProfileInfo
        fields=('portfolio_site','profile_pic')
        widgets={
        'portfolio_site':forms.TextInput(attrs={
                            'class':'form-control',
                            'placeholder':'Enter you Website here...',

        }),
        }
