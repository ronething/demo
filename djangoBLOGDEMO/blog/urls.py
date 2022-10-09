# coding=utf-8

from django.conf.urls import url

from blog import views

urlpatterns = (
    url(r'^$', views.index),
    url(r'^model$', views.model_test),
    url(r'^articles$', views.all_articles),
    url(r'^article/(?P<article_id>[0-9]+)$', views.one_article, name='article_page'),
)
