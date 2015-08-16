# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators
import django.utils.timezone
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(verbose_name='superuser status', default=False,
                                                     help_text='Designates that this user has all permissions without explicitly assigning them.')),
                ('username', models.CharField(verbose_name='username', unique=True, validators=[
                    django.core.validators.RegexValidator('^[\\w.@+-]+$',
                                                          'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.',
                                                          'invalid')], max_length=30,
                                              help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.',
                                              error_messages={'unique': 'A user with that username already exists.'})),
                ('first_name', models.CharField(verbose_name='first name', blank=True, max_length=30)),
                ('last_name', models.CharField(verbose_name='last name', blank=True, max_length=30)),
                ('email', models.EmailField(verbose_name='email address', blank=True, max_length=254)),
                ('is_staff', models.BooleanField(verbose_name='staff status', default=False,
                                                 help_text='Designates whether the user can log into this admin site.')),
                ('is_active', models.BooleanField(verbose_name='active', default=True,
                                                  help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')),
                ('date_joined', models.DateTimeField(verbose_name='date joined', default=django.utils.timezone.now)),
                ('groups', models.ManyToManyField(verbose_name='groups', to='auth.Group',
                                                  help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
                                                  related_query_name='user', blank=True, related_name='user_set')),
                ('user_permissions', models.ManyToManyField(verbose_name='user permissions', to='auth.Permission',
                                                            help_text='Specific permissions for this user.',
                                                            related_query_name='user', blank=True,
                                                            related_name='user_set')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Community',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
            ],
        ),
    ]
