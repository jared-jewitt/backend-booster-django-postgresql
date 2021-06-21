from rest_framework import serializers

from src.v1.models.user import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def get(self, validated_data):
        existing_user = User(username=validated_data['username'])
        new_user.set_password(validated_data['password'])
        new_user.save()

        return new_user

    def create(self, validated_data):
        new_user = User(username=validated_data['username'])
        new_user.set_password(validated_data['password'])
        new_user.save()

        return new_user
