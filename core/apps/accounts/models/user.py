from django.db import models
from django.contrib.auth.models import AbstractUser

from core.apps.shared.models.base import BaseModel


class User(AbstractUser, BaseModel):
    tg_id = models.CharField(max_length=20, null=True, blank=True) 


