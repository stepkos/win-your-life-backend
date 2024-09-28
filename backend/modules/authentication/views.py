import uuid
from datetime import datetime, timedelta

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

from config import settings
from modules.authentication.exceptions import ActivationTokenExpiredException
from modules.authentication.models import CustomUser, ActivationToken
from modules.authentication.serializers import (
    CustomTokenObtainPairSerializer,
    RegisterSerializer,
    ActivationSerializer,
)
from modules.emails.services import create_message, send_email
from modules.users.user_service import UserService


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="Register",
        description="Register a new user",
        parameters=[
            OpenApiParameter(
                name="email", description="email of new user", required=True, type=str
            ),
            OpenApiParameter(
                name="password",
                description="password of new user",
                required=True,
                type=str,
            ),
        ],
        responses={200: str},  # Define response type
    )
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        auth_user = serializer.create(serializer.validated_data)
        UserService().create_user(serializer.data["email"])

        email = serializer.data["email"]

        atoken = ActivationToken.objects.create(
            user=auth_user,
            expiration_date=datetime.now() + timedelta(days=1),
            id=uuid.uuid4(),
        )
        atoken.save()

        message_text = f"Hi {email}, you are about to start your journey with Win Your Life application. To activate your account, please click the link below:\n\nhttp://{settings.HOST_NAME}:{settings.APPLICATION_PORT}/api/activation/{atoken.id}"

        message = create_message(
            from_="Win Your Life Team",
            to=serializer.data["email"],
            subject="Activate your account",
            body=message_text,
        )
        send_email(
            message=message,
            login=settings.EMAIL_LOGIN,
            password=settings.EMAIL_PASSWORD,
            receiver=serializer.data["email"],
        )

        return Response({"content": "User created"})


class ActivationView(APIView):
    permission_classes = (AllowAny,)

    @extend_schema(
        summary="Activate account",
        description="Activate account",
        responses={200: str},  # Define response type
    )
    def get(self, request, token_id):
        token = ActivationToken.objects.get(id=token_id)

        if token.expiration_date < datetime.now():
            raise ActivationTokenExpiredException("Activation token expired")

        user = token.user
        user.is_active = True
        user.save()
        return Response({"content": "User activated"})
