import uuid as uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None

    email = models.CharField(max_length=25, unique=True)
    phone = models.CharField(max_length=10, **NULLABLE)
    country = models.CharField(max_length=25, **NULLABLE)
    avatar = models.ImageField(upload_to='users/', **NULLABLE)
    is_active = models.BooleanField(default=False)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
