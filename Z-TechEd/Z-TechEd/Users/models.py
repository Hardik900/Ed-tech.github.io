from datetime import datetime

from django.contrib import auth
from django.db import models
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User



# Create your models here.
class Detail_user(models.Model):
    def __str__(self):
        return '%s %s' % (self.Firstname, self.Lastname)

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Firstname = models.CharField(max_length=20)
    Lastname = models.CharField(max_length=20, default=None)
    coursename = models.CharField(max_length=20, default=None)
    certificate_id = models.CharField(max_length=10, default=get_random_string(length=10))
    date = models.DateTimeField(default=datetime.now)


