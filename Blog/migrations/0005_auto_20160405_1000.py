# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-05 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20160405_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_subject',
            field=models.TextField(max_length=1000),
        ),
    ]
