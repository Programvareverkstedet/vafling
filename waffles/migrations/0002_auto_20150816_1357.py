# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('waffles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timeFrom', models.DateTimeField()),
                ('timeTo', models.DateTimeField()),
                ('description', models.TextField()),
                ('community', models.ForeignKey(to='waffles.Community')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField()),
                ('payers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Subevent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.BooleanField(default=datetime.datetime(2015, 8, 16, 13, 56, 47, 395852, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='timeFrom',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 13, 56, 56, 586943, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='timeTo',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 16, 13, 57, 0, 178924, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subevent',
            name='event',
            field=models.ForeignKey(to='waffles.Event'),
        ),
        migrations.AddField(
            model_name='subevent',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='subevent',
            field=models.ForeignKey(to='waffles.Subevent'),
        ),
    ]
