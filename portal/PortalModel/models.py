from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os

# Create your models here.
class UserExtension(User):
    nickname = models.CharField(max_length=50)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.email, filename)


class Data(models.Model):
    # filename = models.CharField(max_length=70)
    createtime = models.DateTimeField(default=timezone.now)
    # position = models.CharField(max_length=300)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    datafile = models.FileField(upload_to=user_directory_path)
    description = models.CharField(max_length=200)
    datatype = models.IntegerField(default=0)

    @property
    def filename(self):
        return os.path.basename(self.datafile.name)

    
