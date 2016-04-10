# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-03 20:03
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
                ('subject', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/articles')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('views', models.IntegerField(default='0')),
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
                ('published', models.BooleanField(default=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('comment_content', models.CharField(max_length=1000)),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
                ('replay', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
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
                ('comment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Comment')),
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
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('image', models.ImageField(default='images_folder/none/no-img.jpg', upload_to='images_folder/users')),
                ('active', models.BooleanField(default=False)),
                ('role', models.IntegerField(default='2')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
        migrations.AddField(
            model_name='article',
            name='user_id',
            field=models.ForeignKey(default='1000', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
