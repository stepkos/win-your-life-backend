from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from modules.users.serializers import UserSerializer, ChangeUserFriendsSerializer, ChangeUserSerializer, \
    UserProfileSerializer
from modules.users.user_service import UserService


# Create your views here.


class UserFriendsView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get All user's friends",
        description="Get All user's friends",
        responses={200: UserSerializer}
    )
    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        friends = user.friends.all()
        return Response({'content': UserSerializer(friends, many=True).data})

    @extend_schema(
        summary="Add one friend",
        description="Add one friend",
        parameters=[OpenApiParameter(name='friend_email', description='email of friend to add', required=True, type=str)],
        responses={200: str}
    )
    def post(self, request):
        user = UserService().get_user_by_email(request.user.email)
        UserService().add_friend(user, request.data)
        return Response({'content': 'Friend added'})

    @extend_schema(
        summary="Delete one friend",
        description="Delete one friend",
        parameters=[OpenApiParameter(name='friend_email', description='email of friend to delete', required=True, type=str)],
        responses={200: str}
    )
    def delete(self, request):
        user = UserService().get_user_by_email(request.user.email)
        UserService().remove_friend(user, request.data)
        return Response({'content': 'Friend removed'})

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get user profile info",
        description="Get user profile",
        responses={200: UserProfileSerializer}
    )
    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        return Response({'content': UserProfileSerializer(user.user_profile).data})

    @extend_schema(
        summary="Update user profile",
        description="Update user profile",
        parameters=[OpenApiParameter(name='is_dark_mode', description='is dark mode', required=True, type=bool),
                    OpenApiParameter(name='is_private', description='is private', required=True, type=bool)],
        responses={200: str}
    )
    def put(self, request):
        user = UserService().get_user_by_email(request.user.email)
        user_profile = user.user_profile
        validated_data = UserProfileSerializer(data=request.data)
        validated_data.is_valid(raise_exception=True)
        validated_data.update(user_profile, validated_data.validated_data)
        return Response({'content': 'Profile updated'})

class UserView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        summary="Get user info",
        description="Get user info",
        responses={200: UserSerializer}
    )
    def get(self, request):
        user = UserService().get_user_by_email(request.user.email)
        return Response({'content': UserSerializer(user).data})

    @extend_schema(
        summary="Change user email",
        description="Change user email",
        parameters=[OpenApiParameter(name='email', description='new email', required=True, type=str)],
        responses={200: str}
    )
    def put(self, request):
        user = UserService().get_user_by_email(request.user.email)
        validated_data = ChangeUserSerializer(data=request.data)
        validated_data.is_valid(raise_exception=True)
        user.email = validated_data.validated_data['email']
        user.save()
        return Response({'content': 'Email changed'})
