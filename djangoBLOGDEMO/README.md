# djangoBLOGDEMO

## dev

- `python manage.py sqlmigrate [app] [prefix_id]` 查看 sql 语句

```
$ python manage.py sqlmigrate blog 0001                       
BEGIN;
--
-- Create model Article
--
CREATE TABLE "blog_article" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "title" varchar(52) NOT NULL, "content" text NULL);
COMMIT;
```

- makemigrations migrate

makemigrations 会在当前目录下生成一个migrations文件夹，该文件夹的内容就是数据库要执行的内容 

`python manage.py makemigrations`

migrate 就是执行之前生成的 migrations 文件，这一步才是操作数据库的一步 

`python manage.py migrate`

- django template 支持对象传递

- 通过创建 `templates/[app]` 指定对应的模版文件

- 模版可以直接使用对象

- 创建超级用户

`python manage.py createsuperuser`

- 配置 admin

在 app 下 admin.py 引入自身的 models

`admin.site.register(models.xxxx)`

- 超链接

`{% url 'app_name:url_name' param %}`

- 修改数据

```
article.title = 'xxx'
article.save()
```

- templates 过滤器

可以修改模版中的变量，从而显示不同的内容

怎么使用过滤器 `{{ value|filter }}`

`{{ value|default:'0'}}`

- django shell

自动引入了项目环境

`python manage.py shell`

- admin filter 过滤器

`list_filter`

## qa

- 明明只是创建了一个 model

```
# ronething @ ronethings-mac-pro in ~/PycharmProjects/djangoBLOGDEMO [14:02:24] 
$ python manage.py makemigrations                                                            
Migrations for 'blog':
  blog/migrations/0001_initial.py
    - Create model Article
# ronething @ ronethings-mac-pro in ~/PycharmProjects/djangoBLOGDEMO [14:03:01] 
$ python manage.py migrate                                                                   
Operations to perform:
  Apply all migrations: admin, auth, blog, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying blog.0001_initial... OK
  Applying sessions.0001_initial... OK
```

其实是 INSTALLED_APPS 里面的 app 迁移

- namespace

https://blog.csdn.net/zoulonglong/article/details/79612973

- 设置 csrf token

`{% csrf_token %}`