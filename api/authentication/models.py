import os
import secrets
from django.core.validators import validate_email
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager

from django.utils.timezone import now

from helper.generator import Generator


def get_avatar_path(instance, filename):
    filename, file_extension = os.path.splitext(filename)
    return "userfiles/%s/avatar/%s.%s" % (instance.hash, secrets.token_hex(32), file_extension)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.PositiveIntegerField(default=Generator.generate_pk, primary_key=True)
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, blank=True, null=True, validators=[validate_email])
    full_name = models.CharField(default='', blank=True, max_length=32)
    phone = models.CharField(max_length=32, blank=True, default=None, null=True)
    avatar = models.ImageField(upload_to=get_avatar_path, null=True, default=None, blank=True, max_length=256)
    bio = models.CharField(max_length=256, default='', blank=True)
    type = models.PositiveSmallIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_created = models.DateTimeField(default=now, blank=True)
    last_login = models.DateTimeField(default=None, null=True, blank=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    class Admin:
        list_display = ('username', 'full_name', 'date_created', 'last_login')
        search_fields = ('username__icontains',)
