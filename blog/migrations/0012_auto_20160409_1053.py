# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-09 10:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20160409_0846'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='view',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='view',
            name='view_article',
        ),
        migrations.RemoveField(
            model_name='view',
            name='view_user',
        ),
        migrations.DeleteModel(
            name='View',
        ),
    ]