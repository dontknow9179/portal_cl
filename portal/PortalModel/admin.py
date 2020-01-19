from django.contrib import admin

# Register your models here.
from .models import UserExtension, File

admin.site.register(UserExtension)
admin.site.register(File)