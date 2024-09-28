import uuid

from rest_framework import serializers

from authapp.models import Client


class ClientSerizalizer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Client.objects.create(
            id = uuid.uuid4(),
            email=validated_data['email'],
            password=validated_data['password']
        )

    def to_representation(self, instance):
        return {
            'email': instance.email,
            'date_created': instance.date_created
        }
