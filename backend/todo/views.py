from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from .models import Group, ToDo
from .serializers import GroupSerializer, ToDoSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    '''
    An endpoint that allows you to create
    a new group or get and edit your own groups
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(owner=user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)
    

class ToDoViewSet(viewsets.ModelViewSet):
    '''
    Edpoint that allows the user to
    interact with the todos in their groups
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        group = get_object_or_404(
            Group,
            pk=self.kwargs['group_id'],
            owner = self.request.user,
            )
        serializer.save(group=group)

    def get_queryset(self):
        qs = super().get_queryset()
        group = get_object_or_404(
            Group,
            pk = self.kwargs['group_id'],
            owner = self.request.user,
        )
        return qs.filter(
            group = group,
            )


