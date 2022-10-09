from django.contrib import admin

# Register your models here.

from blog.models import Article


class ArticleAdmin(admin.ModelAdmin):
    """注册a article admin"""
    list_display = ('title', 'content')


admin.site.register(Article, ArticleAdmin)
