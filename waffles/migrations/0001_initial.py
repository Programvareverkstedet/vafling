# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, blank=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='superuser status',
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username',
                 models.CharField(max_length=30, error_messages={'unique': 'A user with that username already exists.'},
                                  verbose_name='username', validators=[
                         django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                               'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                                               'invalid')], unique=True,
                                  help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.')),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status',
                                                 help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(default=True, verbose_name='active',
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(related_name='user_set',
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  to='auth.Group', blank=True, verbose_name='groups',
                                                  related_query_name='user')),
                ('user_permissions',
                 models.ManyToManyField(related_name='user_set', help_text='Specific permissions for this user.',
                                        to='auth.Permission', blank=True, verbose_name='user permissions',
                                        related_query_name='user')),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User profiles',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Community name')),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Community members')),
            ],
            options={
                'verbose_name': 'Community',
                'verbose_name_plural': 'Communities',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Event name')),
                ('description', models.TextField(verbose_name='Description/text')),
                ('open', models.BooleanField(verbose_name='Open for new participants')),
                ('status', models.BooleanField(verbose_name='Finalized')),
                ('timeFrom', models.DateTimeField(verbose_name='Start time')),
                ('timeTo', models.DateTimeField(verbose_name='End time')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Participants')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timeFrom', models.DateTimeField(verbose_name='Start time')),
                ('timeTo', models.DateTimeField(verbose_name='End time')),
                ('description', models.TextField(verbose_name='Description/text')),
                ('community', models.ForeignKey(to='waffles.Community', verbose_name='Community')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Requesting user')),
            ],
            options={
                'verbose_name': 'Listing',
                'verbose_name_plural': 'Listing',
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('payers', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Payers')),
            ],
            options={
                'verbose_name': 'Shopping list',
                'verbose_name_plural': 'Shopping lists',
            },
        ),
        migrations.CreateModel(
            name='SubEvent',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('event', models.ForeignKey(to='waffles.Event', verbose_name='Parent event')),
                ('participants', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='Participants')),
            ],
            options={
                'verbose_name': 'Sub Event',
                'verbose_name_plural': 'Sub Events',
            },
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='subevent',
            field=models.ForeignKey(to='waffles.SubEvent', verbose_name='Connected sub-event'),
        ),
    ]
