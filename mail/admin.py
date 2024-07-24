from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Mail)
class MailAdmin(admin.ModelAdmin):
    list_display = ("uid", "email")