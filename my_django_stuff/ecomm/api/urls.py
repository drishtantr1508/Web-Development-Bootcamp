from django.urls import include , path
from .views import *

urlpatterns=[
    path('',home,name="api-home"),
    path('category/',include('api.category.urls'))

]
