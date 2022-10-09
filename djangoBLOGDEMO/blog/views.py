from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from blog import models


def index(request):
    # return HttpResponse("hello world")
    send = dict(word="hello blog.")
    return render(request, "blog/index.html", send)


def model_test(request):
    """数据库 model 测试"""
    article = models.Article.objects.get(pk=1)
    return render(request, 'blog/model.html', dict(article=article))


def all_articles(request):
    """所有文章"""
    articles = models.Article.objects.all()
    return render(request, 'blog/articles.html', dict(articles=articles))

def one_article(request, article_id):
    """文章详情"""
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'blog/model.html', dict(article=article))