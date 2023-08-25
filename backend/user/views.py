from django.contrib.auth import authenticate, login
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model

from .serializers import UserSerializer


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = UserSerializer


@api_view(('POST',))
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username is None or password is None:
        return Response({
            "errors": {
                "__all__": "Please enter both username and password"
            }
        }, status=400)
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({"detail": "Success"})
    return Response(
        {"detail": "Invalid credentials"},
        status=400,
    )