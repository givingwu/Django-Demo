# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

def index(request):
  # query all
  articles = models.Article.objects.all()
  return render(request, 'blog/index.html', { 'articles': articles })

def article_page(request, article_id):
  # query only one
  article = models.Article.objects.get(pk=article_id)
  return render(request, 'blog/article.html', { 'article': article })

def edit_page(request, article_id):
  if str(article_id) == '0':
    return render(request, 'blog/edit.html')
  else:
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/edit.html', { 'article': article })

def edit_action(request):
  title = request.POST.get('title', 'TITLE')
  content = request.POST.get('content', 'CONTENT')
  models.Article.objects.create(title=title, content=content)

  article_id = request.POST.get('article_id', '0')

  if article_id == '0':
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', { 'articles': articles })
  else:
    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request, 'blog/article.html', { 'article': article })