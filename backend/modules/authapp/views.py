from django.shortcuts import render
from rest_framework import generics

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView

from modules.authapp.models import CustomUser
from modules.authapp.serializers import CustomTokenObtainPairSerializer, RegisterSerializer


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#Register User
class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class Register(APIView):

    def post(self, request):
        ClientService.register(request.data)
        return Response({'message': 'Client created successfully'})

class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({'content':request.user.username})




