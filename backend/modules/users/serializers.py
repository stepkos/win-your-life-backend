from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    is_dark_mode = serializers.BooleanField(required=True)
    is_private = serializers.BooleanField(required=True)

    def to_representation(self, instance):
        return {
            "is_dark_mode": instance.is_dark_mode,
            "is_private": instance.is_private,
        }

    def update(self, instance, validated_data):
        instance.is_dark_mode = validated_data.get(
            "is_dark_mode", instance.is_dark_mode
        )
        instance.is_private = validated_data.get("is_private", instance.is_private)
        instance.save()
        return instance


class UserInfoChangeNameSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get("first_name", instance.first_name)
        instance.last_name = validated_data.get("last_name", instance.last_name)
        instance.save()
        return instance


class UserInfoAddStreakSerializer(serializers.Serializer):
    streak = serializers.IntegerField(required=True)

    def update(self, instance, validated_data):
        instance.streak = validated_data.get("streak", instance.streak)
        instance.save()
        return instance


class UserInfoSerializer(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)

    def to_representation(self, instance):
        return {
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "streak": instance.streak,
        }


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    user_profile = UserProfileSerializer()
    friends = serializers.ListField(child=serializers.EmailField())

    def to_representation(self, instance):
        return {
            "email": instance.email,
            "user_profile": UserProfileSerializer(instance.user_profile).data,
            "user_info": UserInfoSerializer(instance.user_info).data,
            "friends": [friend.email for friend in instance.friends.all()],
        }


class ChangeUserFriendsSerializer(serializers.Serializer):
    friend_email = serializers.EmailField(required=True)


class ChangeUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
