# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('waffles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', models.IntegerField(verbose_name='Amount owed')),
                ('date', models.DateTimeField(verbose_name='Date integrated')),
            ],
            options={
                'verbose_name': 'Calculation',
                'verbose_name_plural': 'Calculations',
            },
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('amount', models.BigIntegerField(verbose_name='Amount owed')),
                (
                'debtee', models.ForeignKey(verbose_name='Debtee', related_name='debtee', to=settings.AUTH_USER_MODEL)),
                (
                'debtor', models.ForeignKey(verbose_name='Debtor', related_name='debtor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Total debt',
                'verbose_name_plural': 'Total debts',
            },
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('date', models.DateField(verbose_name='Date made')),
                ('amount', models.IntegerField(verbose_name='Amount owed')),
                ('debt', models.ForeignKey(verbose_name='Connected debt', to='mercantile.Debt')),
            ],
            options={
                'verbose_name': 'Cash settlement',
                'verbose_name_plural': 'Cash settlements',
            },
        ),
        migrations.AddField(
            model_name='calculation',
            name='debt',
            field=models.ForeignKey(verbose_name='Connected debt', to='mercantile.Debt'),
        ),
        migrations.AddField(
            model_name='calculation',
            name='event',
            field=models.ForeignKey(to_field='Connected event', to='waffles.Event'),
        ),
    ]
