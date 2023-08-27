from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet, ToDoViewSet


router = DefaultRouter()
router.register(r'groups', GroupViewSet)
router.register(r'groups/(?P<group_id>[0-9]+)/todo', ToDoViewSet)

urlpatterns = router.urls