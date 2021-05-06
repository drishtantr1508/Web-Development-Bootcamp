from rest_framework.permissions import BasePermission

class MyPermission(BasePermission):
    def has_permission(self, request,view):
        if request.method == 'POST':
            email = request.data.get("email")
            password = request.data.get("password")
            print(email, password)
            if email == 'drishtant@gmail.com' and password == 'shakoor@123':
                print("Request Authorised!2")
                return True
            
        return False