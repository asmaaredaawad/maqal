import re
from django import forms
from django.contrib.auth.models import User
from django.db import models
from .models import UserProfile,Article
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from captcha.fields import ReCaptchaField

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    # captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('first_name','last_name', 'username', 'email', 'password', 'confirm_password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user_image',)

class ArticleForm(forms.ModelForm):
    article_description = forms.CharField(label='Article Title', max_length=100)
    article_subject= forms.CharField(label='Article Subject', max_length=100)
    article_content = forms.CharField(label='Article Content',widget=forms.Textarea)
    article_image = forms.ImageField(label='Article Image')


