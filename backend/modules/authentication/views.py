from django.shortcuts import render
from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication

from rest_framework_simplejwt.views import TokenObtainPairView

from modules.authentication.models import CustomUser
from modules.authentication.serializers import CustomTokenObtainPairSerializer, RegisterSerializer
from modules.users.user_service import UserService


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="Register",
        description="Register a new user",
        parameters=[OpenApiParameter(name='email', description='email of new user', required=True, type=str),
                    OpenApiParameter(name='password', description='password of new user', required=True, type=str)],
        responses={200: str}  # Define response type
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        UserService().create_user(serializer.data['email'])
        return Response({'content': 'User created'})


#
# class Profile(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         return Response({'content':request.user.email})




