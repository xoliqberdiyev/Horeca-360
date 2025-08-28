from django.db import models
from django.contrib.auth.models import AbstractUser

from core.apps.shared.models.base import BaseModel


class User(AbstractUser, BaseModel):
    pass 


