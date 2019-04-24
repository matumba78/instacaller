from django.contrib import admin
from instacaller.models import UserDB,UserContactDB
# Register your models here.
admin.site.register(UserContactDB)
admin.site.register(UserDB)