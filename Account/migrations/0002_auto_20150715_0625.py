# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='account',
            name='tagline',
        ),
        migrations.AddField(
            model_name='account',
            name='campus',
            field=models.CharField(max_length=40, blank=True),
        ),
        migrations.AddField(
            model_name='account',
            name='courses_pack',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='courses_used',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='account',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
    ]
