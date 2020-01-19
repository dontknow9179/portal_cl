from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserExtension(User):
    nickname = models.CharField(max_length=50)


class File(models.Model):
    filename = models.CharField(max_length=70)
    createtime = models.DateTimeField(default=timezone.now)
    position = models.CharField(max_length=300)
    email = models.CharField(max_length=150)