from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError

from .models import Group, ToDo
from .serializers import GroupSerializer, ToDoSerializer

# Create your views here.
class GroupViewSet(viewsets.ModelViewSet):
    '''
    An endpoint that allows you to create
    a new group or get and edit your own groups.
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        """
        Checking how many groups a user has.
        """
        max_records = 5
        user = self.request.user
        
        groups_count = Group.objects.filter(owner=user).count()
        if groups_count >= max_records:
            raise ValidationError({
                'detail': f'You cannot have more than {max_records} groups',
            })
        serializer.save(owner=user)
    
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner = self.request.user)
    

class ToDoViewSet(viewsets.ModelViewSet):
    '''
    Edpoint that allows the user to
    interact with the todos in their groups.
    '''
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer

    def perform_create(self, serializer):
        """
        Checking the existence of a group
        and the number of entries in it.
        """
        max_records = 50
        user = self.request.user

        group = get_object_or_404(
            Group,
            pk=self.kwargs['group_id'],
            owner = self.request.user,
            )
        groups_count = group.todo_set.count()
        if groups_count >= max_records:
            raise ValidationError({
                'detail': f'You cannot have more than {max_records} todo records',
            })
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


