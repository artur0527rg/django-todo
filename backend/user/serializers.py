from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", "email", 'avatar',)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        """
        validators.validate_password(password=value)
        return make_password(value)
    
    def validate_avatar(self, value):
        value.name = 'avatar'
        return value