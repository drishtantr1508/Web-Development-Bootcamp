from django.shortcuts import render
from form_app.models import Address, User
from . import forms
# Create your views here.
def homepage(request):
    address_list=Address.objects.order_by()
    user_list=User.objects.order_by()
    list2=zip(user_list,address_list)#Note that you can not use full fledged python in django templates.
    # that is why i have zipped my list here and not in the templates when using for loop.
    #note that when you find it difficult to implement in templates, use all your python knowledge here to succeed.
    home_dict={'user_info':user_list,'address_info':address_list,'list2':list2}
    return render(request,'form_app/homepage.html',context=home_dict)
def formpage(request):
    form=forms.FormName()
    if request.method=='POST':
        form=forms.FormName(request.POST)#form now contains request.POST as a form data.
        if form.is_valid():
            # print("VALIDATION SUCESSFULL!!")
            print('NAME: '+form.cleaned_data['First_name']+" "+form.cleaned_data['Last_name'])
            print('Email: '+form.cleaned_data['Email'])
            print('Contact: '+str(form.cleaned_data['contact']))
            users=User(first_name=form.cleaned_data['First_name'],last_name=form.cleaned_data['Last_name'],Email=form.cleaned_data['Email'],mobile_no=form.cleaned_data['contact'])
            users.save()
            addresses=Address(user=users,address=form.cleaned_data['Address'])
            addresses.save()
        #     form.save(commit=True)
        #     return homepage(request)
        # else:
        #     print("Error!")
    return render(request,'form_app/formpage.html',{'form':form})
def urlpage(request):
    url_dict={}
    return render(request,'form_app/urlpage.html',context=url_dict)
