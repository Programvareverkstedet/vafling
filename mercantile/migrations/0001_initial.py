# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('waffles', '0002_auto_20150816_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('amount', models.BigIntegerField()),
                ('debtee', models.ForeignKey(related_name='debtee', to=settings.AUTH_USER_MODEL)),
                ('debtor', models.ForeignKey(related_name='debtor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('dato', models.DateField()),
                ('amount', models.IntegerField()),
                ('debt', models.ForeignKey(to='mercantile.Debt')),
            ],
        ),
        migrations.AddField(
            model_name='calculation',
            name='debt',
            field=models.ForeignKey(to='mercantile.Debt'),
        ),
        migrations.AddField(
            model_name='calculation',
            name='event',
            field=models.ForeignKey(to='waffles.Event'),
        ),
    ]
