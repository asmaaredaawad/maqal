# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-04 16:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_content', models.CharField(max_length=1000)),
                ('article_subject', models.CharField(max_length=100)),
                ('article_description', models.CharField(blank=True, max_length=200, null=True)),
                ('article_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/articles')),
                ('article_date', models.DateTimeField(auto_now_add=True)),
                ('article_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('article_published', models.BooleanField(default=False)),
                ('article_views', models.IntegerField(default='0')),
                ('article_author', models.ForeignKey(default='1000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Banned_word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_published', models.BooleanField(default=False)),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('comment_last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('comment_content', models.CharField(max_length=1000)),
                ('comment_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Article')),
                ('comment_replay', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Blog.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emotion_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/emotions')),
                ('expression', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Comment')),
                ('like_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='System_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/users')),
                ('marked_articles', models.ManyToManyField(blank=True, null=True, to='Blog.Article')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='article_tags',
            field=models.ManyToManyField(blank=True, null=True, to='Blog.Tag'),
        ),
    ]