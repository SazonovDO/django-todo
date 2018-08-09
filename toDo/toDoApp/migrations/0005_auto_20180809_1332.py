# Generated by Django 2.0.7 on 2018-08-09 13:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('toDoApp', '0004_auto_20180807_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setoftask',
            name='tasks',
        ),
        migrations.AddField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='setOfTask',
        ),
    ]
