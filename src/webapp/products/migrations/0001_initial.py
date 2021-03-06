# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-25 22:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=39.99, max_digits=19)),
                ('image', models.ImageField(blank=True, null=True, upload_to='products')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='products')),
            ],
        ),
    ]
