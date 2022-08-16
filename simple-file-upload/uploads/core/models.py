from __future__ import unicode_literals

from django.db import models

class downloadCSV(models.Model):
    file_name = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=4,blank=True)

class downloadPrevCSV(models.Model):
    file_name = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=4,blank=True)