from datetime import datetime

from django.db import models

# Create your models here.

class Device(models.Model):
    mac = models.CharField(max_length=36)
    ip = models.GenericIPAddressField()
    # a device could not have an account registered if the login is with out user or password
    account = models.CharField(max_length=20)
    last_login = models.DateTimeField('last login', default=datetime.now)
    logged_in = models.BooleanField(default=False)
    hotspot = models.CharField(max_length=20)


