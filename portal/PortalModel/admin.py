from django.contrib import admin

# Register your models here.
from .models import UserExtension, Data, Task

admin.site.register(UserExtension)
admin.site.register(Data)
admin.site.register(Task)