from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from django.contrib.auth.models import User as AuthUser
from django.utils.translation import ugettext_lazy as _

from .models import *

# Register your models here.


class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

#User actions and filters
class UserAdmin(UserAdmin):
	list_display =['username','first_name','last_name','last_login','is_active','is_staff','is_superuser','date_joined','email']
	inlines = (UserProfileInline,)
	actions = ['Active_user','make_superuser','make_stuff','make_regular_user','Deactive_user']
	def make_superuser(self, request, queryset):
		rows_updated = queryset.update(is_staff=False,is_superuser=True)
		if rows_updated == 1:
			message_bit = "1 User was"
		else:
			message_bit = "%s User's were" % rows_updated
		self.message_user(request, "%s successfully setting as SuperUser." % message_bit)
	make_superuser.short_description = "Set useres as SuperUser"

	def make_stuff(self, request, queryset):
		rows_updated = queryset.update(is_staff=True,is_superuser=False)
		if rows_updated == 1:
			message_bit = "1 User was"
		else:
			message_bit = "%s User's were" % rows_updated
		self.message_user(request, "%s successfully setting as Stuff." % message_bit)
	make_stuff.short_description = "Set user as Stuff"

	def make_regular_user(self, request, queryset):
		rows_updated = queryset.update(is_staff=False , is_superuser=False)
		if rows_updated == 1:
			message_bit = "1 User was"
		else:
			message_bit = "%s User's were" % rows_updated
		self.message_user(request, "%s successfully setting as Regular User." % message_bit)
	make_regular_user.short_description = "Set user as Regular User"
	
	def Active_user(self, request, queryset):
		rows_updated = queryset.update(is_active=True)
		if rows_updated == 1:
			message_bit = "1 User was"
		else:
			message_bit = "%s User's were" % rows_updated
		self.message_user(request, "%s successfully Activte." % message_bit)
	Active_user.short_description = "Avtivate user"
	
	def Deactive_user(self, request, queryset):
		rows_updated = queryset.update(is_staff=False , is_superuser=False,is_active=False)
		if rows_updated == 1:
			message_bit = "1 User was"
		else:
			message_bit = "%s User's were" % rows_updated
		self.message_user(request, "%s successfully Deactivte." % message_bit)
	Deactive_user.short_description = "Deavtivate user"

# set Artical action and filters:
class ArticalePublishedListFilter(admin.SimpleListFilter):
    title = _('Is Published')
    parameter_name = 'published'
    def lookups(self, request, model_admin):
        return (
            ('is_published', _('published')),
            ('not_published', _('Not published')),
        )
    def queryset(self, request, queryset):        
        if self.value() == 'is_published':
            return queryset.filter(article_published=True)
        if self.value() == 'not_published':
            return queryset.filter(article_published=False)

class ArticleAdmin(admin.ModelAdmin):
	list_display =['article_author','article_subject','article_description','article_published','article_image','article_content','article_date','article_last_updated','article_views']
	list_filter = (ArticalePublishedListFilter,)
	actions = ['published_article','unpublished_article']
	def published_article(self, request, queryset):
		rows_updated = queryset.update(article_published=True)
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully marked as published." % message_bit)
	published_article.short_description = "Mark selected stories as published"

	def unpublished_article(self, request, queryset):
		rows_updated = queryset.update(article_published=False)
		if rows_updated == 1:
			message_bit = "1 story was"
		else:
			message_bit = "%s stories were" % rows_updated
		self.message_user(request, "%s successfully marked as unpublished." % message_bit)
	unpublished_article.short_description = "Mark selected stories as unpublished"

# set Comment action and filters:
class CommentPublishedListFilter(admin.SimpleListFilter):
    title = _('Is Published')
    parameter_name = 'published'
    def lookups(self, request, model_admin):
        return (
            ('is_published', _('published')),
            ('not_published', _('Not published')),
        )
    def queryset(self, request, queryset):        
        if self.value() == 'is_published':
            return queryset.filter(comment_published=True)
        if self.value() == 'not_published':
            return queryset.filter(comment_published=False)

class CommentAdmin(admin.ModelAdmin):
	list_display =['comment_article','comment_published','comment_content','comment_date','comment_last_updated','comment_replay']
	list_filter = (CommentPublishedListFilter,)
	actions = ['published_comment','unpublished_comment']
	def published_comment(self, request, queryset):
		rows_updated = queryset.update(comment_published=True)
		if rows_updated == 1:
			message_bit = "1 Comment was"
		else:
			message_bit = "%s Comments were" % rows_updated
		self.message_user(request, "%s successfully marked as published." % message_bit)
	published_comment.short_description = "Mark selected Comments as published"

	def unpublished_comment(self, request, queryset):
		rows_updated = queryset.update(comment_published=False)
		if rows_updated == 1:
			message_bit = "1 Comment was"
		else:
			message_bit = "%s Comments were" % rows_updated
		self.message_user(request, "%s successfully marked as unpublished." % message_bit)
	unpublished_comment.short_description = "Mark selected Comments as unpublished"

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Like)
admin.site.register(Emotion)
admin.site.register(System_status)

