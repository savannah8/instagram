# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-06-25 06:58
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0006_auto_20190625_0954'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profileid',
        ),
    ]
