from django.db import models

# Create your models here.

class Registration(models.Model):
    first = models.CharField("First", max_length=50)
    last = models.CharField("Last", max_length=50)
    email = models.EmailField()