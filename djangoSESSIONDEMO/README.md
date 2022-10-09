# django session test

测试 django session 存储

## process

- session_engine 配置

默认 `SESSION_ENGINE = 'django.contrib.sessions.backends.db'`

使用数据库进行 session 存储

如果数据库中没有对应的表 在进行存储的时候会产生报错

![database 中没有对应表](https://i.loli.net/2019/08/13/njyK93lJEO1WUtb.png)

此次主要是为了测试实现 cookie-based-sessions 即数据加密存储在 cookie 中

配置 `settings.py`

`SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'`

![效果](https://i.loli.net/2019/08/13/3DXGVqtE89AKZsl.png)

- 基本使用

存储：`request.session['user'] = 'panda'`

取值：`request.session.get('user')`

## 0x0F

- https://docs.djangoproject.com/en/2.2/topics/http/sessions/#using-cookie-based-sessions
- https://segmentfault.com/a/1190000016041458