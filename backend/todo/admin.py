from django.contrib import admin

from .models import Group, ToDo

# Register your models here.
admin.site.register(Group)
admin.site.register(ToDo)