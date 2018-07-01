# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Authenticate(models.Model):
    userName = models.CharField(max_length=20)
    token = models.CharField(max_length=100)
    isActive = models.BooleanField(default=1)

class SMSData(models.Model):
    smsFrom = models.CharField(default=0,max_length=16)
    smsTo = models.CharField(default=0,max_length=16)
    smsText = models.CharField(max_length=121)
    smsTime = models.DateTimeField(auto_now_add=True)
    smsUser = models.ForeignKey(Authenticate)
