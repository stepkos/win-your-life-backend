import uuid

from modules.authentication.models import CustomUser
from modules.users.models import User, UserProfile, UserInfo
from modules.users.serializers import ChangeUserFriendsSerializer


class UserService:
    def get_user_by_email(self, email):
        return User.objects.get(email=email)

    def create_user(self, email):
        return User.objects.create(
            id=uuid.uuid4(),
            email=email,
            user_profile=UserProfile.objects.create(id=uuid.uuid4()),
            user_info=UserInfo.objects.create(id=uuid.uuid4()),
        )

    def add_friend(self, user, data):
        validated_data = ChangeUserFriendsSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        friend = UserService().get_user_by_email(validated_data.data["friend_email"])
        user.friends.add(friend)
        user.save()

    def remove_friend(self, user, data):
        validated_data = ChangeUserFriendsSerializer(data=data)
        validated_data.is_valid(raise_exception=True)
        friend = UserService().get_user_by_email(validated_data.data["friend_email"])
        user.friends.remove(friend)
        user.save()
