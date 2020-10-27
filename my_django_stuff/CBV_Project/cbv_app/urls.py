from django.conf.urls import url
from django.urls import path
from cbv_app import views
app_name='cbv_app'
urlpatterns=[
    url(r'^$',views.SchoolList.as_view(),name="list"),
    url(r'^(?P<pk>\d+)/$',views.SchoolDetail.as_view(),name="detail"),# pk means link this url with
    # the primary key . on School detail view which renders student detail html page.
    url(r'^create/$',views.SchoolCreateView.as_view(),name="create"),
    url(r'^update/(?P<pk>[-\w]+)/$',views.SchoolUpdateView.as_view(),name="update"),
    url(r'^delete/(?P<pk>[-\w]+)/$',views.SchoolDeleteView.as_view(),name="delete"),
]
