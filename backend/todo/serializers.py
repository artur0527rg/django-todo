from rest_framework import serializers

from .models import Group, ToDo


class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Group
        fields = '__all__'


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'is_checked', 'created_at', 'title')