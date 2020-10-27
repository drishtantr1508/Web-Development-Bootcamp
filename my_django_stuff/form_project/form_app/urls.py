from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from form_app import views
urlpatterns=[
    url(r'^$',views.urlpage,name="urlpage")
 ]
