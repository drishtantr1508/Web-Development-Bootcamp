from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from cbv_app import views
app_name='cbv_app'
urlpatterns=[
    url(r'^$',views.CompanyList.as_view(),name='companylist'),
    url(r'^(?P<pk>\d+)/$',views.CompanyDetail.as_view(),name="detail"),
    url(r'^create/',views.CreateCompany.as_view(),name="create"),
    url(r'^employee/(?P<pk>\d+)/$',views.EmployeeDetail.as_view(),name="employeedetail"),
    url(r'^employeeupdate/(?P<pk>\d+)/$',views.UpdateEmployee.as_view(),name="employeeupdate"),
    url(r'^update/(?P<pk>\d+)/$',views.UpdateCompany.as_view(),name="update"),
    url(r'^register/',views.register,name="register"),
    url(r'^login/',views.user_login,name='login')


]
