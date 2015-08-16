# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
import django.core.validators
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, verbose_name='last login', null=True)),
                ('is_superuser', models.BooleanField(default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.',
                                                     verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, verbose_name='username', validators=[
                    django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                          'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                                          'invalid')], unique=True,
                                              help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(max_length=30, blank=True, verbose_name='first name')),
                ('last_name', models.CharField(max_length=30, blank=True, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, blank=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False,
                                                 help_text='Designates whether the user can log into this admin site.',
                                                 verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                                                  verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups',
                 models.ManyToManyField(related_query_name='user', verbose_name='groups', related_name='user_set',
                                        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                        blank=True, to='auth.Group')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', verbose_name='user permissions',
                                                            related_name='user_set',
                                                            help_text='Specific permissions for this user.', blank=True,
                                                            to='auth.Permission')),
            ],
            options={
                'verbose_name_plural': 'User profiles',
                'verbose_name': 'User profile',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Community name')),
                ('members', models.ManyToManyField(verbose_name='Community members', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Communities',
                'verbose_name': 'Community',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Event name')),
                ('description', models.TextField(verbose_name='Description/text')),
                ('open', models.BooleanField(verbose_name='Open for new participants')),
                ('status', models.BooleanField(verbose_name='Finalized')),
                ('timeFrom', models.DateTimeField(verbose_name='Start time')),
                ('timeTo', models.DateTimeField(verbose_name='End time')),
                ('participants', models.ManyToManyField(verbose_name='Participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Events',
                'verbose_name': 'Event',
            },
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('timeFrom', models.DateTimeField(verbose_name='Start time')),
                ('timeTo', models.DateTimeField(verbose_name='End time')),
                ('description', models.TextField(verbose_name='Description/text')),
                ('community', models.ForeignKey(verbose_name='Community', to='waffles.Community')),
                ('user', models.ForeignKey(verbose_name='Requesting user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Listing',
                'verbose_name': 'Listing',
            },
        ),
        migrations.CreateModel(
            name='ShoppingList',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('payers', models.ManyToManyField(verbose_name='Payers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shopping lists',
                'verbose_name': 'Shopping list',
            },
        ),
        migrations.CreateModel(
            name='SubEvent',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('event', models.ForeignKey(verbose_name='Parent event', to='waffles.Event')),
                ('participants', models.ManyToManyField(verbose_name='Participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sub Events',
                'verbose_name': 'Sub Event',
            },
        ),
        migrations.AddField(
            model_name='shoppinglist',
            name='subevent',
            field=models.ForeignKey(verbose_name='Connected sub-event', to='waffles.SubEvent'),
        ),
    ]
