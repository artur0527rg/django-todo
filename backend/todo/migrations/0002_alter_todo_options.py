# Generated by Django 4.2.4 on 2023-08-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'ordering': ['-created_at'], 'verbose_name': 'ToDo', 'verbose_name_plural': 'ToDo'},
        ),
    ]