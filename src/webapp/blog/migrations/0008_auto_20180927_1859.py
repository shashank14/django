# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-27 18:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_postmodel_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='postmodel',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='slug',
            field=models.SlugField(blank=True, editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(error_messages={'unique': 'title has to be unique'}, help_text='please enter title here', max_length=50, unique=True),
        ),
    ]
