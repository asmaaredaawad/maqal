from django.shortcuts import render,render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.core.context_processors import csrf
from django.contrib.sessions.models import Session
from django.conf import settings
from django.contrib.auth.signals import user_logged_in
from forms import ArticleForm
# from .models import UserSession
# from django.contrib.sessions.models import Session
from .models import *

# Create your views here.
# like
def like(request):
	pass
# Display All Article
def index(request) :
	# if not request.user.id:
	# 	return HttpResponseRedirect('login')
	last_articles=Article.objects.filter(article_published=1).order_by('article_date')[:6];
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	context = {'article':last_articles,'recent':recent,'tags':tags,'user':request.user}
	return render(request,'Blog/index.html',context)
def articles(request):
	articles=Article.objects.filter(article_published=1).order_by('article_date')[:12];
	recent=Article.objects.filter(article_published=1).order_by('article_date')[:2];
	tags=Tag.objects.filter().order_by('id')[:5];
	context = {'artic':articles,'recent':recent,'tags':tags};
	return render(request,'Blog/articles.html',context)
# ___________________________________________________________
# def index(request) :
# 	# if not request.user.id:
# 	# 	return HttpResponseRedirect('login')

# 	articles = Article.objects.all()
# 	context = {'articles':articles,'user':request.user}
# 	return render(request,'Blog/index1.html',context)
# Add Comment
def add(request,article_id):
	if not request.user:
		# raise Http404
		return HttpResponseRedirect('index')
	# add new view to model view
	article = Article.objects.get(pk=article_id)
	article.article_views +=1
	article.save()
	text = request.POST['comments']
	if text is not None and text != '':
		article.article_comments +=1
		new_comment=Comment(comment_content=text,comment_article=article,comment_author=request.user)
		new_comment.save()
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	context = {'user':request.user,'comments':comments, 'article':article}
	return render(request,'Blog/details.html',context)

def createArticle(request):	
	if request.method == 'POST':
		form = ArticleForm(request.POST,request.FILES)
		title=request.POST.get('article_description')
		
		subject=request.POST.get('article_subject')
		image=request.POST.get('article_image')
		date =request.POST.get('article_date')
		new_article= Article(article_description=title,article_subject=subject,article_image=image,article_date=date)
		new_article.save()
		return HttpResponse("Aricle added successfully")
	else:
		form = ArticleForm()
	return render(request,'Blog/createArticle.html',{"Name":request.user.username,'form': form})



	# related article
def relatedArticle(request,article_id):
	article=Article.objects.get(pk=article_id)
	# tags=article.tag_set.all()
	tags=article.article_tags.all()
	word=tags[0]
	print word
	tag=Tag.objects.get(tag=word)
	rel_art=tag.article_set.all()
	return render(request,'Blog/details.html',{'article':article,'rel_art':tags})


			

# Edit Article
def editart(request,article_id):
	text = request.POST['article']
	article=Article.objects.filter(pk=article_id).update(article_content=text)
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	context = {'comments':comments, 'article':article}
	return render(request,'Blog/details.html',context)
# Edit Comment
def editcomm(request,comment_id,article_id):
	if not request.user:
		return HttpResponseRedirect('Blog/index.html')
	text=request.POST['comments']
	comment=Comment.objects.filter(pk=comment_id).update(comment_content=text)
	articles = Article.objects.get(pk=article_id)
	comments = articles.comment_set.all()
	context = {'comments':comments, 'article':articles}
	return render(request,'Blog/details.html',context)


def single_article(request,article_id):
	article = Article.objects.get(pk=article_id)
	output = "<h5><pre><a href='#'>Home     Articles     Sign In     Sign Up      Facebook Login  </a></pre></h5>"
	output += "<h4>"+article.subject+"</h4>"
	output += "<p>"+article.article_content+"</p>"
	output += str(article.image)+"</br></hr>"
	# ......comments for each article....
	comments = article.comment_set.all()
	for comment in comments:
		output += "<h2>Comments</h2>"+comment.comment_content+"</br></hr>"

	#......add comment......
	# comment = request.POST['comment']
	# new_comment=Comment(comment_content=comment,article_id=article)
	# new_comment.save()
	return render(request,'Blog/index.html',output)


def login(request):
	if request.COOKIES.get("sessionid",None):
		return HttpResponseRedirect('/Blog/loggedin')
	c= {}
	c.update(csrf(request))
	return render_to_response('Blog/login.html',c)

def auth_view(request):
	username=request.POST.get('username')
	password=request.POST.get('password')
	user=authenticate(username=username,password=password)
	if not request.POST.get('remember_me'):
		request.session.set_expiry(0)
	if user is not None:
		auth.login(request,user)
		return HttpResponseRedirect('/Blog/loggedin')
	else:
		return HttpResponseRedirect('/Blog/invalid')

		

def loggedin(request):
	return render(request,'Blog/loggedin.html')

def invalid(request):
	return render(request,'Blog/invalid.html')

def logout(request):
	auth.logout(request)
	return render(request,'Blog/logout.html')



def user_logged_in_handler(sender, request, user, **kwargs):
	UserSession.objects.get_or_create(user = user, session_id = request.session.session_key)
	user_logged_in.connect(user_logged_in_handler)
	# session = Session.objects.get(session_key=session_key)
	uid = session.get_decoded().get('_auth_user_id')
	user = User.objects.get(pk=uid)
	return HttpResponse(user)
	# r2ba5mfn99qospi1khzw30y6jb8jy61m

	# print user.username, user.get_full_name(), user.email



def delete_user_sessions(user):
    user_sessions = UserSession.objects.filter(user = user)
    for user_session in user_session:
        user_session.session.delete()	


			

		
					

		


