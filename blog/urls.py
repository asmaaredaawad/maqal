from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^(?P<article_id>[0-9]+)/add$',add),
    url(r'^(?P<article_id>[0-9]+)/add_comment$',add_comment),
    url(r'^(?P<article_id>[0-9]+)/editart$',editart),
    url(r'^(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/editcomm$',editcomm),
    url(r'^login/$',login),
    url(r'^articles/$',articles),
    url(r'^auth/$',auth_view),
    url(r'^logout/$',logout),
    url(r'^loggedin/$',loggedin),
    url(r'^invalid/$',invalid),







]
