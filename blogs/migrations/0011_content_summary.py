# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2019-01-13 14:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_post_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='summary',
            field=models.TextField(default=None),
        ),
    ]