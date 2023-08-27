from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import GroupViewSet


router = DefaultRouter()
router.register(r'groups', GroupViewSet)

urlpatterns = router.urls