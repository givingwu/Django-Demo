# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ( 'title', 'content', 'pub_time', ) # it supports `list` and `tuple` too.
  list_filter = ( 'pub_time', ) # add new filter

# register Article model to admin.site.
admin.site.register(Article, ArticleAdmin)