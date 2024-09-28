from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from modules.auth.client_service import ClientService


class Login(APIView):
    def post(self, request):

        token = ClientService.login(request.data)
        return Response({'token':token})

class Register(APIView):

    def post(self, request):
        ClientService.register(request.data)
        return Response({'message': 'Client created successfully'})

class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, email):
        return Response({'content':ClientService.get_client_by_email(email)})




