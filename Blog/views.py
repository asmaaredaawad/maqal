from django.shortcuts import render

from django.http import HttpResponse

from .models import *

# Create your views here.

# Display All Article
def index(request) :
	articles = Article.objects.all()
	context = {'articles':articles}
	return render(request,'index.html',context)
# Add Comment
def add(request,article_id):
	article = Article.objects.get(pk=article_id)
	article.article_views +=1
	article.save()
	text = request.POST['comments']
	new_comment=Comment(comment_content=text,comment_article=article)
	new_comment.save()
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	context = {'comments':comments, 'article':article}
	return render(request,'details.html',context)

	# related article
def relatedArticle(request,article_id):
	article=Article.objects.get(pk=article_id)
	# tags=article.tag_set.all()
	# tag=Tag.objects.filter(tag__in =tags)
	# articles=article.objects.filter(article_tags__in=tags)
	# articles = get_list_or_404( Article,article_tags__in='os')
	return render(request,'details.html',{'article':article})

			

# Edit Article
def editart(request,article_id):
	text = request.POST['article']
	article=Article.objects.filter(pk=article_id).update(article_content=text)
	article = Article.objects.get(pk=article_id)
	comments = article.comment_set.all()
	context = {'comments':comments, 'article':article}
	return render(request,'details.html',context)
# Edit Comment
def editcomm(request,comment_id,article_id):
	text=request.POST['comments']
	comment=Comment.objects.filter(pk=comment_id).update(comment_content=text)
	articles = Article.objects.get(pk=article_id)
	comments = articles.comment_set.all()
	context = {'comments':comments, 'article':articles}
	return render(request,'details.html',context)


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

