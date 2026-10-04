from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)
    wechat = models.CharField(max_length=30, blank=True)
    # 可增加更多字段
    class Meta(AbstractUser.Meta):
        pass



