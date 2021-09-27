from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models as coreM
# Register your models here.
admin.site.register(coreM.User)
