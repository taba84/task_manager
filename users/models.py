from django.db import models
from django.contrib.auth.models import User, Group
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    """Profile model for django users, get it with user.get_profile()"""
    user = models.OneToOneField(User, primary_key=True)
    last_login_source = models.CharField(max_length=15)


class Groups(models.Model):
    """Users group"""
    group_name = models.OneToOneField(Group)
    creation_time = models.DateTimeField(default=timezone.now())


