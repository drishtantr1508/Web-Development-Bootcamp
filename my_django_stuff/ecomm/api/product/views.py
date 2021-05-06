from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .custompermissions import MyPermission
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.



# class ProductViewSet(viewsets.ModelViewSet):
#     # permission_classes = [MyPermission]
#     queryset = Product.objects.all().order_by('id')
#     serializer_class = ProductSerializer
# @permission_classes((permissions.AllowAny,))
class ProductList(APIView):
    # permission_classes = [MyPermission]
    # def get(self, request):
    #     product = Product.objects.all()
    #     serializer = ProductSerializer(product,many=True)
    #     return Response(serializer.data)
    permission_classes = [MyPermission]
    def post(self, request):
        # email = request.data.get("email")
        # password = request.data.get("password")
        # print(email, password)
        # if email == 'drishtant@gmail.com' and password == 'shakoor@123':
        #     print("Request Authorised!")
        #     # return True
        #     product = Product.objects.all()
        #     serializer = ProductSerializer(product,many=True)
        #     return Response(serializer.data)
        
        product = Product.objects.all()
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data)