# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-24 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0002_auto_20190624_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='images',
        ),
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
    ]
