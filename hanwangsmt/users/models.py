from django.db import models

# Create your models here.
import uuid

from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    #uid
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #电话
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'user'
        verbose_name = '用户管理'
        verbose_name_plural = verbose_name
