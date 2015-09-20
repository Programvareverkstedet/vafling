# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mercantile', '0001_initial'),
        ('waffles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt',
            name='debtee',
            field=models.ForeignKey(related_name='debtee', to=settings.AUTH_USER_MODEL, verbose_name='Debtee'),
        ),
        migrations.AddField(
            model_name='debt',
            name='debtor',
            field=models.ForeignKey(related_name='debtor', to=settings.AUTH_USER_MODEL, verbose_name='Debtor'),
        ),
        migrations.AddField(
            model_name='calculation',
            name='debt',
            field=models.ForeignKey(to='mercantile.Debt', verbose_name='Connected debt'),
        ),
        migrations.AddField(
            model_name='calculation',
            name='event',
            field=models.ForeignKey(to='waffles.Event', verbose_name='Connected event'),
        ),
    ]
