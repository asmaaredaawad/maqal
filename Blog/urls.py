from django.conf.urls import url
from django.contrib import admin
from Blog.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^(?P<article_id>[0-9]+)/article/$',single_article),
    url(r'^(?P<article_id>[0-9]+)/rel$',relatedArticle),
    url(r'^(?P<article_id>[0-9]+)/add$',add),
    url(r'^(?P<article_id>[0-9]+)/editart$',editart),
    url(r'^(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/editcomm$',editcomm)


]
