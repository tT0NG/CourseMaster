# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_account_is_vip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_premium',
        ),
        migrations.AddField(
            model_name='account',
            name='courses_failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
