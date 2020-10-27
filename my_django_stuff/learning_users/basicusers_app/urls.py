from django.contrib import admin
from django.urls import path
from django.conf.urls import url , include
from basicusers_app import views
app_name='basicusers_app'
urlpatterns=[
    url(r'^register/',views.register,name='register'),
    url(r'^login/',views.login,name='login')

]
