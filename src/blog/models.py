# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Article(models.Model):
  # if u use python3, use `__str__(self)`
  # otherwise use `__unicode__(self)`
  title = models.CharField(max_length=32, default="title")
  content = models.TextField(null=True)
  pub_time = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.title
