from django.db import models
import uuid
from django.contrib.auth.models import (
    BaseUserManager, AbstractUser, PermissionsMixin
)

class User(AbstractUser):
    email = models.EmailField('email address', blank=True, unique=True)
    surname = models.CharField(max_length=255, null=True, blank=True)
    nin = models.CharField(max_length=255, null=True, blank=True)

    is_active = models.BooleanField('active status', default=True)
    is_admin = models.BooleanField('admin status', default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
