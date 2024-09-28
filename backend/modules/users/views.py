from multiprocessing.connection import Client

from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.users.serializers import UserSerializer, ChangeUserFriendsSerializer, ChangeUserSerializer, \
    UserProfileSerializer
from modules.users.user_service import UserService


# Create your views here.


class UserFriendsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        friends = user.friends.all()
        return Response({'content': UserSerializer(friends, many=True).data})

    def post(self, request):
        user = UserService().get_user_by_email(request.user.email)
        UserService().add_friend(user, request.data)
        return Response({'content': UserSerializer(user.friends.all(), many=True).data})

    def put(self, request):
        user = UserService().get_user_by_email(request.user.email)
        UserService().remove_friend(user, request.data)
        return Response({'content': UserSerializer(user.friends.all(), many=True).data})

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        return Response({'content': UserProfileSerializer(user.user_profile).data})

    def put(self, request):
        user = UserService().get_user_by_email(request.user.email)
        user_profile = user.user_profile
        validated_data = UserProfileSerializer(data=request.data)
        validated_data.is_valid(raise_exception=True)
        validated_data.update(user_profile, validated_data.validated_data)

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        return Response({'content': UserSerializer(user).data})

    def put(self, request):
        user = UserService().get_user_by_email(request.user.email)
        validated_data = ChangeUserSerializer(data=request.data)
        validated_data.is_valid(raise_exception=True)
        user.email = validated_data.validated_data['email']
        user.save()
