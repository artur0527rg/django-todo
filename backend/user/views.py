from django.contrib.auth import get_user_model
from rest_framework.generics import (
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    GenericAPIView,
)

from .serializers import UserSerializer
from .permissions import IsAuthenticatedOrCreateOnly


User = get_user_model()


class UserAPIView(CreateAPIView,
                  RetrieveAPIView,
                  UpdateAPIView,
                  DestroyAPIView,
                  GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrCreateOnly,)

    def get_object(self):
        return self.request.user