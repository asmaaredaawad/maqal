# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-10 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160409_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_description',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_replay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Comment'),
        ),
    ]