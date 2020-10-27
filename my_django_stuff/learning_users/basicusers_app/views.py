from django.shortcuts import render
from django.http import HttpResponse
from basicusers_app.forms import UserForm,UserProfileInfoForm
# Create your views here.
def homepage(request):
    return render(request,'basicusers_app/homepage.html')
def register(request):

    registerd=False

    if request.method == 'POST':
        user_form=UserForm(data=request.POST)
        profile_form=UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in 'request.FILES':
                profile.profile_pic=request.FILES['profile_pic']

            profile.save()

            registerd=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(request,'basicusers_app/register.html',{'registerd':registerd,'user_form':user_form,'profile_form':profile_form})

def login(request):
    return render(request,'basicusers_app/login.html')
