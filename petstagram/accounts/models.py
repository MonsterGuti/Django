from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from accounts.managers import AppUserManager


class AppUser(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = "email"
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = AppUserManager()

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.URLField(blank=True, null=True)

