from rest_framework import serializers


class UserProfileSerializer(serializers.Serializer):
    is_dark_mode = serializers.BooleanField(required=True)
    is_private = serializers.BooleanField(required=True)

    def to_representation(self, instance):
        return {
            'is_dark_mode': instance.is_dark_mode,
            'is_private': instance.is_private
        }

    def update(self, instance, validated_data):
        instance.is_dark_mode = validated_data.get('is_dark_mode', instance.is_dark_mode)
        instance.is_private = validated_data.get('is_private', instance.is_private)
        instance.save()
        return instance



class UserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    user_profile = UserProfileSerializer()
    friends = serializers.ListField(child=serializers.EmailField())

    def to_representation(self, instance):
        return {
            'email': instance.email,
            'user_profile': UserProfileSerializer(instance.user_profile).data,
            'friends': [friend.email for friend in instance.friends.all()]
        }

class ChangeUserFriendsSerializer(serializers.Serializer):
    friend_email = serializers.EmailField(required=True)

class ChangeUserSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
