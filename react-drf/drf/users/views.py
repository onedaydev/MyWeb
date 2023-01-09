from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework import views
from rest_framework.response import Response

from .serializers import *


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data

        response = Response({"token": token.key}, status=status.HTTP_200_OK)
        response.set_cookie('auth_token', token, httponly=True, samesite='strict')
        return response
    
class LogoutView(views.APIView):
    def post(self, request):
        response = Response({'message':'logout success'})
        response.delete_cookie('auth_token')
        return response