from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.context_processors import csrf
from django.contrib.sessions.models import Session
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from .models import *


# Create your views here.

# Display All Article
def index(request) :
	# if not request.user.id:
	# 	return HttpResponseRedirect('login')
	last_articles=Article.objects.filter(article_published=1).order_by('article_date')[:6];
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	user_id = request.user.id
	if user_id:
		user_image = UserProfile.objects.get(user_id=user_id)
		context = {'article':last_articles,'recent':recent,'tags':tags,'user_image':user_image,'user':request.user}
	else:
		context = {'article':last_articles,'recent':recent,'tags':tags,'user':request.user}
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/index.html',context)

def articles(request):
	articles=Article.objects.filter(article_published=1).order_by('article_date')[:12];
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	user_id = request.user.id
	if user_id:
		user_image = UserProfile.objects.get(user_id=user_id)
		context = {'article':articles,'recent':recent,'tags':tags,'user_image':user_image};
	else:
		context = {'article':articles,'recent':recent,'tags':tags};
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/articles.html',context)
# Add Comment
def add(request,article_id):
	if not request.user:
		# raise Http404
		return HttpResponseRedirect('index')
	# add new view to model view
	article = Article.objects.get(pk=article_id)
	article.article_views +=1
	article.save()
	
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	user_id = request.user.id
	if user_id:
		user_image = UserProfile.objects.get(user_id=user_id)
		context = {'user':request.user,'user_image':user_image,'comments':comments, 'article':article,'recent':recent,'tags':tags}
	else:
		context = {'user':request.user,'comments':comments, 'article':article,'recent':recent,'tags':tags}
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/single.html',context)

def add_comment(request,article_id):
	text = request.POST['comment']
	article = Article.objects.get(pk=article_id)
	if text is not None and text != '':
		article.article_comments +=1
		new_comment=Comment(comment_content=text,comment_article=article,comment_author=request.user)
		new_comment.save()
	
	article.article_views +=1
	article.save()
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	context = {'user':request.user,'comments':comments, 'article':article,'recent':recent,'tags':tags}
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/single.html',context)
# def add_comment_replay(request,article_id,comment_id):
# 	text = request.POST['replay']
# 	if text is not None and text != '':
# 		new_comment=Comment(comment_content=text,comment_article=article,comment_author=request.user)
# 		new_comment.save()
# 	article = Article.objects.get(pk=article_id)
# 	article.article_views +=1
# 	article.save()
# 	article = Article.objects.get(pk=article_id)
# 	comments = article.comment_set.all()
# 	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
# 	tags=Tag.objects.filter().order_by('id')[:5];
# 	context = {'user':request.user,'comments':comments, 'article':article,'recent':recent,'tags':tags}
# 	return render(request,'blog/single.html',context)
	# article
# def createArticle(request):
# 	if request.POST :
# 		form = ArticleForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return HttpResponseRedirect('/Blog')
# 	else :
# 		form = ArticleForm()
# 	c={}
# 	c.update(csrf(request))
# 	c['form']= form
# 	return render_to_response('Blog/createArticle.html',c)	


	# related article

# Edit Article
def editart(request,article_id):
	text = request.POST['article']
	subj = request.POST['subject']
	desc = request.POST['description']
	pub = request.POST['published']
	article=Article.objects.filter(pk=article_id).update(
		article_content=text,
		article_subject=subj,
		article_description=desc,
		article_published=desc,
		)
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	context = {'comments':comments, 'article':article}
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/single.html',context)
# Edit Comment
def editcomm(request,comment_id,article_id):
	if not request.user:
		return HttpResponseRedirect('blog/index.html')
	text=request.POST['comments']
	comment=Comment.objects.filter(pk=comment_id).update(comment_content=text)
	articles = Article.objects.get(pk=article_id)
	comments = articles.comment_set.all()
	context = {'comments':comments, 'article':articles}
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/details.html',context)

def login(request):
	if request.COOKIES.get("sessionid",None):
		return HttpResponseRedirect('/blog/index')
	c= {}
	c.update(csrf(request))
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render_to_response('blog/login.html',c)

def auth_view(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	user=authenticate(username=username,password=password)
	if not request.POST.get('remember_me'):
		request.session.set_expiry(0)
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/blog/')
	else:
		return HttpResponseRedirect('/blog/invalid')

		

def loggedin(request):
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/')

def invalid(request):
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/invalid.html')

def logout(request):
	auth.logout(request)
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return render(request,'blog/login.html')



def user_logged_in_handler(sender, request, user, **kwargs):
	UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)
	user_logged_in.connect(user_logged_in_handler)
	# session = Session.objects.get(session_key=session_key)
	uid = session.get_decoded().get('_auth_user_id')
	user = User.objects.get(pk=uid)
	lock = System_status.objects.all()[:1].get()
	if lock.status :
		return render(request,'blog/locked.html')
	return HttpResponse(user)
	# r2ba5mfn99qospi1khzw30y6jb8jy61m

	# print user.username, user.get_full_name(), user.email



def delete_user_sessions(user):
    user_sessions = UserSession.objects.filter(user = user)
    for user_session in user_session:
		user_session.session.delete()
		


			