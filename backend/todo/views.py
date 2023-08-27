from django.shortcuts import render
from rest_framework import viewsets

from .models import Group
from .serializers import GroupSerializer
from .permissions import IsOwner

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    '''
    An endpoint that allows you to create
    a new group or get and edit your own groups
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsOwner,)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)
