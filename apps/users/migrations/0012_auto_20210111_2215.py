# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-11 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20210111_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.TextField(default='static/images/timg.jpg', verbose_name='图片'),
        ),
        migrations.AlterField(
            model_name='article',
            name='desc',
            field=models.TextField(default='', verbose_name='文章简介'),
        ),
    ]