from __future__ import unicode_literals
from django.contrib.auth.models import *
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Tag(models.Model):
	tag=models.CharField(max_length=20)
	def __str__(self):
		return self.tag 

class Article(models.Model):
	article_author=models.ForeignKey(User,default='1000',on_delete=models.CASCADE)
	article_content=models.CharField(max_length=1000)
	article_subject=models.TextField(max_length=1000)
	article_description=models.CharField(max_length=200,null=True,blank=True)
	article_image=models.ImageField()
	article_date=models.DateTimeField(auto_now_add=True , auto_now=False )
	article_last_updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
	article_published=models.BooleanField(default=False)
	article_views=models.IntegerField(default='0')
	article_tags = models.ManyToManyField(Tag,null=True,blank=True)
	def __str__(self):
		return self.article_subject

class UserProfile(models.Model):
	user = models.OneToOneField(User,null=True,blank=True)
	user_image=models.ImageField(upload_to = 'images_folder/users' , default = 'images_folder/none/no-img.jpg')
	marked_articles = models.ManyToManyField(Article,null=True,blank=True)


class Comment(models.Model):
	comment_article=models.ForeignKey(Article,on_delete=models.CASCADE)
	comment_published=models.BooleanField(default=False)
	comment_date=models.DateTimeField(auto_now_add=True)
	comment_last_updated=models.DateTimeField(auto_now_add=False,auto_now=True,null=True,blank=True)
	comment_content=models.CharField(max_length=1000)
	comment_replay = models.OneToOneField('self',null=True,blank=True)
	def __str__(self):
		return self.comment_content

	def children(self): #replies in comment
		return Comment.objects.filter(comment_replay=self)
		
        

class Like(models.Model):
	like_user=models.ForeignKey(User,on_delete=models.CASCADE)
	like_comment=models.ForeignKey(Comment,on_delete=models.CASCADE)

class Banned_word(models.Model):
	word=models.CharField(max_length=20)
	def __str__(self):
		return self.word

class Emotion(models.Model):
	emotion_image=models.ImageField(upload_to = 'images_folder/emotions' , default = 'images_folder/none/no-img.jpg')
	expression=models.CharField(max_length=10)
	def __str__(self):
		return self.emotion_image

class System_status(models.Model):
	status=models.BooleanField()
	def __str__(self):
		return self.status
