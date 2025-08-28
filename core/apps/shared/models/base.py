import uuid

from django.db import models



class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, unique=True, default=uuid.uuid4)
    created_at = models.DateTimeField(auto_created=True)

    class Meta:
        abstract = True
