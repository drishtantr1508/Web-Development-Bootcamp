from django.shortcuts import render
from django.http import HttpResponse
from MTV_app.models import Address , User
# Create your views here.
def homepage(request):
    home_dict={}
    return render(request,'MTV_app/homepage.html',context=home_dict)
def userpage(request):
    address_list=Address.objects.order_by()
    user_list=User.objects.order_by("first_name")

    user_dict={'info':'Your Recent User information is saved in admin/Mtv_app/user',
    'user_records':user_list,'address_records':address_list,}
    return render(request,'MTV_app/userpage.html',context=user_dict)
