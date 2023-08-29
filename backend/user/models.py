from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django_resized import ResizedImageField


# Create your models here.
class User(AbstractUser):
   email = models.EmailField(unique=True, null=False, blank=False)
   avatar = ResizedImageField(
      size=[720, 720],
      crop=['middle', 'center'],
      upload_to=settings.MEDIA_ROOT,
      null=False,
      blank=False,
      default='avatar.png',
      force_format='PNG',
   )