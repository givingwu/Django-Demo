# how to create a Django-Project?
[Django Project](http://djangoproject.com)
<br/>
[Django Tutorial](https://docs.djangoproject.com/en/2.1/intro/tutorial01/)

## Install
python2.7
```bash
pip install Django==1.11.15
```

python3
```bash
pip3 install Django==1.11.15
```

## Editors
Pycharm
Sublime Text
Atom
Visual Studio code

## Create new project
```bash
django-admin startproject myblog
```

## Run Server
```bash
python manage.py runserver
# custom HOST PORT
python manage.py runserver 8888
```

## File Directory
```
- wsgi.py(Python Web Server Gateway Interface: Python服务器网关接口，Python应用与Web服务器之间的接口)
- urls.py(URL配置文件)
- settings.py(项目的总配置文件)
```

## Create New Application
Step 1:
```bash
python manage.py startapp blog
```

Step 2:
添加该应用到`settings.py`中到`INSTALLED_APPS`。

Step 3:
/blog/*
```
/migrations 数据移植（迁移）模块
  __init__.py
admin.py 该应用后台管理系统到配置文件
apps.py 当前应用的配置
models.py 数据模块，使用ORM框架
tests.py 自动化测试模块
views.py 执行响应的逻辑代码
```

### blog/views.py 界面逻辑：
每个响应对应一个函数，函数必须返回一个响应。
函数必须存在一个参数，一般约定为request。
每一个响应函数对应一个 URL。

### app/urls.py
每个 URL 都以 url 的形式写出来。
url函数放在 urlpatterns 列表中。
url函数有三个参数：URL,method,name

### 包含其他url，如 'blog/index':
在根 urls.py 中引入 include。
在 glob 目录下创建 urls.py，格式与 app/urls.py 相同。

**PS**:
1. 根 urls.py 针对 APP 配置的 URL 名称，是该 APP 所有 URL 的总路径
2. 配置URL是注意正则表达式结尾符号 $ /

## Create 1st HTML template
Django 模版语言， DTL（Django Template language）

DTL初步使用：
1. render(request, 'template.html', dict{ key: val }) 函数中支持一个 dict 类型参数
2. 该字典是后台传递到模版的参数，键为参数名
3. 在模版中使用 {{参数名}} 来直接使用

1. 创建 templates 目录
2. 创建 templates/{name}.html

**PS:**
+ Django 按照 `INSTALLED_APPS`中的添加顺序查找`Templates`。
+ 不同APP下的`Templates`目录中的同名`.html`文件会造成冲突。

**How to resolve?**
+ 在APP的`templates` 目录下创建以 `app` 为名称的目录。
+ 将 `{appName}/templates/{appName}/{name}.html` 文件放入新创建的目录下。

## Models in Django
+ Per model mapping a database table.
+ Model is `class` based in Django.
+ It includes some basic fields and actions.

### What is ORM?
+ Object Relation Mapping, like Java Hibernate.
+ Impls object and database mapping.
+ Do not use any SQL words.

### How to write a model?
+ Create a new file `models.py` in root directory, and imports `models` module.
+ Create a new class and it extends `models.Model`, it is a database table in fact.
+ Create key in Model(It is a field in database table actually), `attr = models.CharField(mx_length=64)`

### How to generates a table in connected database?
+ get into `manage.py` use terminal.
+ type `python manage.py makemigrations {appName*}` and executes it.
+ type `python manage.py migrate` and executes this command again.

### Where to find the file after generated and migrated?
+ Where is the file after migrated? - `{appName}/migrations`

### How to generates SQL sentences?
+ type `python manage.py sqlmigrate {appName} 0001:order` and executes it.


## How to use dynamic data from SQL DB?
+ `views.py` 中 `import models`
+ ORM sentence: `article = models.Article.objects.get(pk=1)`
+ Render dynamic data: `render(request, page, { 'article': 'article 123' })`

## Admin 管理
+ `Admin` 是 `Django` 自带的一个功能强大的 `自动化数据管理界面`。
+ 被授权的用户可以直接在 `Admin` 中管理数据库。
+ Django 提供了许多针对 `Admin` 个性化配置。

### How to create a user for admin system?
+ type `python manage.py createsuperuser` and executes it.
+ Wanna modify admin web language? modify attr `LANGUAGE_CODE='zh_Hans'` in `app/setting.py`.
+ Customization `admin.py` model, just import it from self's `models` then register it to `admin.site.register(Article)`.
+ Customization model name if u use python3, use `__str__(self)` otherwise use `__unicode__(self)`.

### Complete Blog pages
1. '/blog/index': blogs list page
  + `{% for item in [] %}`
  + `{% endfor %}`
2. '/blog/:id': blog content page
  + 动态传参 `url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page)`
  + (?P=<groupName>) 必须与 `views.py` 中特定 `controller` 函数的 `def group(request, groupName)` 一致
3. '/blog/edit': create/write/edit new blog

## Use dynamic link in Django
1. After `href` is the `target link`
2. In template could use `{% url 'app_name:url_name' param %}`

## Use dynamic form iin Django
1. Use `request.POST['ParamName']` to get the field data
2. Use `models.Article.objects.create(title, content)` to create a new model object.

## How to update one dynamic data?
1. `article.title = title` // assertion
2. `article.save()` // invoke `model.save()`

## Templates filter
a little same with `.JSP` and express `.jade`, `.ejs`.

like Frontend `angular`, `vue` MVVM frame-work filter syntax:
```python
{{ value | filter }}
```

Multiple filters:
```python
{{ value | filter1 | filter2 | ... }}
```

Example:
```html
<input type="hidden" name="article_d" value={{article.id | default:'0' }}>
```

## What's Django shell?
1. It's a CLI program.

## When to use Django shell?
1. Test the new `method` or Look up an object's all `properties` and `methods`.

## How to custom APP admin properties?
1. Create a new config class. `class ArticleAdmin(admin.ModelAdmin)`
2. Register it. `admin.site.register(Article, ArticleAdmin)`