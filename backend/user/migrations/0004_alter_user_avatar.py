# Generated by Django 4.2.4 on 2023-08-29 15:13

from django.db import migrations
import django_resized.forms
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='avatar.png', force_format=None, keep_meta=True, quality=-1, scale=None, size=[720, 720], upload_to=pathlib.PureWindowsPath('C:/MyFiles/Python/django-todo/backend/media')),
        ),
    ]