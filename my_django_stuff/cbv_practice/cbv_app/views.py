from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from cbv_app import models
from . import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
#@login_required
class Homepage(TemplateView):
    template_name='cbv_app/homepage.html'

class CompanyList(ListView):
    context_object_name='companies'
    model=models.Company
    template_name='cbv_app/company_list.html'
class CompanyDetail(DetailView):
    context_object_name='company_detail'
    model=models.Company
    template_name='cbv_app/company_details.html'#note that if you mispelled html file name then it will
    #not show errors , infact it will render a blank white page. basically a html file with no detail.

class CreateCompany(CreateView):
    model=models.Company
    fields="__all__"
    template_name="cbv_app/create_company.html"
    # A context of name form for creating form will automatically be created.

class UpdateCompany(UpdateView):# note that when we use Update view django automatically makes
# template_name= 'company_form.html' and also a context of update form as form is made.
    fields='__all__'
    model=models.Company

class UpdateEmployee(UpdateView):# note that when we use Update view django automatically makes
# template_name= 'company_form.html' and also a context of update form as form is made.
    fields=('name','age')
    model=models.Employee

class EmployeeDetail(DetailView):
    context_object_name='employees'
    model=models.Employee
    template_name='cbv_app/employee_detail.html'


def register(request):
    registered=False
    if request.method=='POST':
        user_form=forms.UserForm(data=request.POST)
        profile_form=forms.UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=forms.UserForm()
        profile_form=forms.UserProfileInfoForm()
    return render(request,'cbv_app/register.html',{'registered':registered,'profile_form':profile_form,'user_form':user_form})


def user_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('homepage'))
            else:
                return HttpResponse("Account is temporarily disabled")
        else:
            return HttpResponse("<h1><b><i>Invalid Details, LogIn Failed</i></b></h1>")
    else:
        return render(request,'cbv_app/login.html',{})
