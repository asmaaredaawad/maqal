from django.conf.urls import url
from django.contrib import admin
from blog.views import *

urlpatterns = [
    url(r'^$',index),
    url(r'^(?P<article_id>[0-9]+)/add$',add),
    url(r'^(?P<article_id>[0-9]+)/add_comment$',add_comment),
    url(r'^(?P<article_id>[0-9]+)/editart$',editart),
    url(r'^(?P<article_id>[0-9]+)/(?P<comment_id>[0-9]+)/editcomm$',editcomm),
    url(r'^register/$',register),
    url(r'^editProfile/$',editProfile),
    url(r'^login/$',login),
    url(r'^articles/$',articles),
    url(r'^auth/$',auth_view),
    url(r'^logout/$',logout),
    url(r'^loggedin/$',loggedin),
    url(r'^invalid/$',invalid),
    url(r'^user/password/reset/$', 
        'django.contrib.auth.views.password_reset', 
        {'post_reset_redirect' : 'Blog/user/password/reset/done/'},
        name="password_reset"),
    url(r'^user/password/reset/done/$',
        'django.contrib.auth.views.password_reset_done'),
   url (r'^user/password/reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 
        'django.contrib.auth.views.password_reset_confirm', 
        {'post_reset_redirect' : 'Blog/user/password/done/'}),
   url (r'^user/password/done/$', 
        'django.contrib.auth.views.password_reset_complete'),







]
