# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-12 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import readbooks.models


class Migration(migrations.Migration):

    dependencies = [
        ('readbooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='profile_picture',
            field=models.ImageField(blank=True, default=1, upload_to=readbooks.models.author_upload_directory),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='cover_picture',
            field=models.ImageField(blank=True, default=1, upload_to=readbooks.models.book_upload_directory),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='critic',
            name='profile_picture',
            field=models.ImageField(blank=True, default=1, upload_to=readbooks.models.critic_upload_directory),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='group',
            name='cover_picture',
            field=models.ImageField(blank=True, default=1, upload_to=readbooks.models.group_upload_directory),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publisher',
            name='cover_picture',
            field=models.ImageField(blank=True, default=1, upload_to=readbooks.models.publisher_upload_directory),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reader',
            name='profile_picture',
            field=models.ImageField(blank=True, default=11, upload_to=readbooks.models.reader_upload_directory),
            preserve_default=False,
        ),
    ]
