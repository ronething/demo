# -*- coding:utf-8 _*-  
""" 
@author: ashing
@time: 2019-08-13 23:19
@mail: axingfly@gmail.com

Less is more.
"""
from django.conf.urls import url
from user import views

urlpatterns = (
    url(r'^login$', views.login),
    url(r'^index$', views.index),
    url(r'^test$', views.test),
)
