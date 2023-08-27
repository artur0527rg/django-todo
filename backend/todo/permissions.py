from rest_framework.permissions import IsAuthenticated

class IsOwner(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner:
            return True
        return False