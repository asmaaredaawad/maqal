from django import forms
import datetime
from .models import Article


class ArticleForm(forms.Form):
    article_description = forms.CharField(label='Article Title', max_length=100)
    article_subject= forms.CharField(label='Article Title', max_length=100)
    article_content = forms.CharField(label='Article Content',widget=forms.Textarea)
    article_image = forms.ImageField(label='Article Image')
    article_date= forms.DateTimeField(label='Published Date' ,input_formats=['%Y-%m-%d %H:%M:%S'],initial=datetime.datetime.today)




     