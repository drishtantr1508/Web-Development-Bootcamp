from django.shortcuts import render
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
@login_required # this will allow user to render view if and only if he is logged in. Very useful decorator
def homepage(request):
    return render(request,'auth_app/homepage.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

@login_required
def special(request):
    return HttpResponse("You are logged in")

def register(request):
    registered=False
    if request.method=='POST':
        user_form=forms.UserForm(request.POST)
        profile_form=forms.UserProfileInfoForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)#here setpassword is an attribute used to set password for the userun
            # here we set user.password which is attribute from user form as password for user
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user# as we know we have linked user with profile info in models.py
            # thus profile.user is that linked user which is equal to user=user_form.save()
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']#similarly here profile_pic
                # is attribute pf profile=profile_form.save(), which is assigned the value profile_pic Key
                # from dictionary request.FILES

            profile.save()
            registered=True

        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=forms.UserForm()
        profile_form = forms.UserProfileInfoForm()
    return render(request,'auth_app/register.html',{'registered':registered , 'profile_form':profile_form,
    'user_form':user_form})


def user_login(request):# when we submit login forms in html page this happens further.
    if request.method=='POST':# to check if its returning something to backend.
        username=request.POST.get('username')#this assigns username fron login page to username variable
        password=request.POST.get('password')#this assigns password from login page to password variable

        user=authenticate(username=username,password=password)# this actually returns a boolean value
        # assigning to user variable. Inbuilt function to determine if both username and password is
        # is correct or not.
        if user:
            if user.is_active:# it checks whether the account is temporarily disabled or not or if
            # account is active or not or blocked or not by superuser.
                login(request,user)#built in django function to login details of user variable.
                return HttpResponseRedirect(reverse("homepage"))

            else:
                return HttpResponse("<h1>Account not active<h1>")
        else:
            print("Someone tried to login and failed.")
            print("Username: {} and Password: {}".format(username,password))
            return HttpResponse("<h1>invalid login details</h1>")
    else:
        return render(request,'auth_app/login.html',{})
