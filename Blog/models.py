from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count
# from django.contrib.comments.models import Comment

# class CommentWithTitle(Comment):
#     title = models.CharField(max_length=300)

# Create your models here.
class Tag(models.Model):
	tag=models.CharField(max_length=20,unique=True)
	def __str__(self):
		return self.tag 

class Article(models.Model):
	article_author=models.ForeignKey(User,default='1',on_delete=models.CASCADE)
	article_subject=models.CharField(max_length=100)
	article_content=models.CharField(max_length=1000)
	article_description=models.CharField(max_length=200,null=True,blank=True)
	article_image=models.ImageField()
	# upload_to = 'images_folder/articles' , default = 'images_folder/none/no-img.jpg'
	article_date=models.DateTimeField(auto_now_add=True , auto_now=False)
	article_last_updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
	article_published=models.BooleanField(default=False)
	article_views=models.IntegerField(default='0')
	article_comments=models.IntegerField(default='0')
	article_tags = models.ManyToManyField(Tag,null=True,blank=True)
	def __str__(self):
		return self.article_subject

class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True,blank=True)
	user_image=models.ImageField()
	# upload_to = 'images_folder/users' , default = 'images_folder/none/no-img.jpg'
	marked_articles = models.ManyToManyField(Article,null=True,blank=True)
	# view_articles = models.ManyToManyField(Article,null=True,blank=True)


class Comment(models.Model):
	comment_author=models.ForeignKey(User,default='1',on_delete=models.CASCADE)
	comment_article=models.ForeignKey(Article,on_delete=models.CASCADE)
	comment_published=models.BooleanField(default=False)
	comment_date=models.DateTimeField(auto_now_add=True)
	comment_last_updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
	comment_content=models.CharField(max_length=1000)
	comment_replay = models.OneToOneField('self',null=True,blank=True)
	comment_count=models.IntegerField(default='0')
	def __str__(self):
		return self.comment_content	
	def childern(self):
		return Comment.object.filter(comment_replay=self)
	@property
	def is_parent(self):
	    if self.comment_replay is not None:
	    	return False
	    return True	
		
						

class Like(models.Model):
	like_user=models.ForeignKey(User,on_delete=models.CASCADE)
	like_comment=models.ForeignKey(Comment,on_delete=models.CASCADE)
	@property
	def total_likes(self):
		return self.like_comment.count()
    
        """
        Likes for the company
        :return: Integer: Likes for the company
        """


class Banned_word(models.Model):
	word=models.CharField(max_length=20)
	def __str__(self):
		return self.word

class Emotion(models.Model):
	emotion_image=models.ImageField()
	# upload_to = 'images_folder/emotions' , default = 'images_folder/none/no-img.jpg'
	expression=models.CharField(max_length=10)
	def __str__(self):
		return self.emotion_image

class System_status(models.Model):
	status=models.BooleanField()
	