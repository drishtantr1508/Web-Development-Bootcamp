from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from MTV_app import views
urlpatterns=[
    url(r'^$',views.userpage,name="homepage"),
]
