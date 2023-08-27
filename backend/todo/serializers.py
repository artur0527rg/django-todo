from rest_framework import serializers

from .models import Group


class GroupSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Group
        fields = '__all__'