from django.conf.urls import url
from django.contrib import admin
from Blog.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^(?P<article_id>[0-9]+)/article/$',single_article),
    url(r'^(?P<article_id>[0-9]+)/rel$',relatedArticle),
    url(r'^(?P<article_id>[0-9]+)/add$',add),
    url(r'^(?P<article_id>[0-9]+)/editart$',editart),
    url(r'^(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/editcomm$',editcomm),
    url(r'^articles/$',articles),
    # login

    url(r'^login/$',login),
    url(r'^auth/$',auth_view),
    url(r'^logout/$',logout),
    url(r'^loggedin/$',loggedin),
    url(r'^invalid/$',invalid),

    # forget password
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : 'done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
    url (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : 'done/'}),
    url (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),
   # form Article
    url(r'^createArticle/$',createArticle),
   







]
