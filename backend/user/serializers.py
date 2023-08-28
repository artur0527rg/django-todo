from rest_framework import serializers
import django.contrib.auth.password_validation as validators
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model # If used custom user model
from rest_framework.validators import UniqueValidator

UserModel = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = UserModel
        fields = ( "id", "username", "password", "email",)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        """
        validators.validate_password(password=value)
        return make_password(value)