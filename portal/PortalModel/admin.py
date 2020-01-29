from django.contrib import admin

# Register your models here.
from .models import UserExtension, Data

admin.site.register(UserExtension)
admin.site.register(Data)