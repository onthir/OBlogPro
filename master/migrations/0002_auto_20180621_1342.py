# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-21 13:42
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=150)),
                ('message', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='MailingList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('head', models.CharField(max_length=150)),
                ('content', models.TextField(max_length=200)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('read', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='blog',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='word_count',
        ),
        migrations.AddField(
            model_name='blog',
            name='publish',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
