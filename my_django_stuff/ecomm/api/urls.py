from django.urls import include , path
from .views import *

urlpatterns=[
    path('',home,name="api-home"),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
]
