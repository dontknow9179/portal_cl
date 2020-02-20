from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import os
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class UserExtension(User):
    nickname = models.CharField(max_length=50)


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return os.path.join('user_' + instance.email, filename)
    # return 'user_{0}/{1}'.format(instance.email, filename)


class Data(models.Model):
    createtime = models.DateTimeField(default=timezone.now)
    nickname = models.CharField(max_length=50)
    email = models.CharField(max_length=150)
    datafile = models.FileField(upload_to=user_directory_path)
    description = models.CharField(max_length=200)
    datatype = models.IntegerField(default=0)

    @property
    def filename(self):
        return os.path.basename(self.datafile.name)

    
@receiver(post_delete, sender=Data)
def submission_delete(sender, instance, **kwargs):
    instance.datafile.delete(False)


class Task(models.Model):
    createtime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    taskname = models.CharField(max_length=70)
    email = models.CharField(max_length=150)
    content = models.CharField(max_length=500)
    description = models.CharField(max_length=200, blank=True)
    state = models.IntegerField(default=0)
    result = models.CharField(max_length=700, blank=True)