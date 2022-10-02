# drfDEMO

## qa

- django 默认路由问题？

`pipenv run python manage,py runserver` 之后 直接访问 127.0.0.1:8000 可以查看到欢迎页面

```python
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
```
