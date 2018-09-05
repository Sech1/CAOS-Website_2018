from django.contrib import admin
from . import models
from . import forms

# Register your models here.

admin.site.register(models.Registration)
admin.site.register(models.MailText)