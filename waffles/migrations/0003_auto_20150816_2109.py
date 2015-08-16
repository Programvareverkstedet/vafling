# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models, migrations
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('waffles', '0002_auto_20150816_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='community',
            options={'verbose_name': 'Community', 'verbose_name_plural': 'Communities'},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event', 'verbose_name_plural': 'Events'},
        ),
        migrations.AlterModelOptions(
            name='listing',
            options={'verbose_name': 'Listing', 'verbose_name_plural': 'Listing'},
        ),
        migrations.AlterModelOptions(
            name='shoppinglist',
            options={'verbose_name': 'Shopping list', 'verbose_name_plural': 'Shopping lists'},
        ),
        migrations.AlterModelOptions(
            name='subevent',
            options={'verbose_name': 'Sub Event', 'verbose_name_plural': 'Sub Events'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'User profile', 'verbose_name_plural': 'User profiles'},
        ),
        migrations.AddField(
            model_name='event',
            name='open',
            field=models.BooleanField(default=datetime.datetime(2015, 8, 16, 19, 9, 38, 507600, tzinfo=utc),
                                      verbose_name='Open for new participants'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='community',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_constraint='Community members'),
        ),
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(verbose_name='Community name', max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Description/text'),
        ),
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(verbose_name='Event name', max_length=64),
        ),
        migrations.AlterField(
            model_name='event',
            name='participants',
            field=models.ManyToManyField(verbose_name='Participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='event',
            name='status',
            field=models.BooleanField(verbose_name='Finalized'),
        ),
        migrations.AlterField(
            model_name='event',
            name='timeFrom',
            field=models.DateTimeField(verbose_name='Start time'),
        ),
        migrations.AlterField(
            model_name='event',
            name='timeTo',
            field=models.DateTimeField(verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='community',
            field=models.ForeignKey(to='waffles.Community', verbose_name='Community'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(verbose_name='Description/text'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='timeFrom',
            field=models.DateTimeField(verbose_name='Start time'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='timeTo',
            field=models.DateTimeField(verbose_name='End time'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Requesting user'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=64),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='payers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_constraint='Payers'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='price',
            field=models.IntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='shoppinglist',
            name='subevent',
            field=models.ForeignKey(to='waffles.SubEvent', to_field='Connected sub-event'),
        ),
        migrations.AlterField(
            model_name='subevent',
            name='event',
            field=models.ForeignKey(to='waffles.Event', to_field='Parent event'),
        ),
        migrations.AlterField(
            model_name='subevent',
            name='name',
            field=models.CharField(verbose_name='Name', max_length=64),
        ),
        migrations.AlterField(
            model_name='subevent',
            name='participants',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, db_constraint='Participants'),
        ),
    ]
