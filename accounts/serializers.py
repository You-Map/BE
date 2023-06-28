from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import Account


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('username', 'email', 'name', 'univ')


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'password', 'name', 'univ')

    def create(self, validated_data):
        user = Account.objects.create_user(**validated_data)
        return user

    def validate_password(self, value):
        validate_password(value)
        return value
