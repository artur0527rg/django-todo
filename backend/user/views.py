from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from .serializers import UserSerializer

User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = UserSerializer(data=request.POST)
    if serialized.is_valid():
        serialized.save()
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)