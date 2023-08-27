from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Group(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=63)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title

class ToDo(models.Model):
    is_checked = models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)

    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo'

    @property
    def owner(self):
        return self.group.owner

    def __str__(self) -> str:
        return self.title