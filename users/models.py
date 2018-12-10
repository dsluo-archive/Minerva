from django.contrib.auth.models import AbstractUser


# Create your models here.
from django.db import models


class CustomUser(AbstractUser):
    email = models.EmailField('email address', unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
