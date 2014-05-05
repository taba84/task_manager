from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Profile(models.Model):
    """Profile model for django users, get it with user.get_profile()"""
    user = models.OneToOneField(User, primary_key=True)
    last_login_source = models.CharField(max_length=15)


class Group(models.Model):
    """Users group"""
    group_name = models.CharField(max_length=50, primary_key=True)
    creation_time = models.DateTimeField(default=timezone.now())


class Users_group(models.Model):
    """Users relationship with group"""
    profile = models.ForeignKey(Profile)
    group = models.ForeignKey(Group)

