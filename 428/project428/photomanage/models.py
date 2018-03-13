from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Photos(models.Model):
	httpurl = models.URLField(max_length=1000)
	category = models.CharField(max_length=200)
def __str__(self):
    return self.httpurl
