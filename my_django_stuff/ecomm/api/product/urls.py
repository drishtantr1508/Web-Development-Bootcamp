from django.urls import path , include
from rest_framework import routers
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

# router = routers.DefaultRouter()
# router.register('',views.ProductViewSet)

urlpatterns = [
    # path('',include(router.urls),name='product'),
    path('list/',views.ProductList.as_view(),name="product list"),
]
