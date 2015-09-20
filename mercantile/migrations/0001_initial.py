# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('amount', models.BigIntegerField(verbose_name='Amount owed')),
            ],
            options={
                'verbose_name': 'Total debt',
                'verbose_name_plural': 'Total debts',
            },
        ),
        migrations.CreateModel(
            name='Settlement',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateField(verbose_name='Date made')),
                ('amount', models.IntegerField(verbose_name='Amount owed')),
                ('debt', models.ForeignKey(to='mercantile.Debt', verbose_name='Connected debt')),
            ],
            options={
                'verbose_name': 'Cash settlement',
                'verbose_name_plural': 'Cash settlements',
            },
        ),
    ]
