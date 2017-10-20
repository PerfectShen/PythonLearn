# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(null=True,blank=True,max_length=200)
    job = models.CharField(null=True,blank=True,max_length=200)
