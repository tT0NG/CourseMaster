# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20150803_0914'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='courses_failed_list',
            field=models.TextField(default=b'[]'),
        ),
        migrations.AddField(
            model_name='account',
            name='is_supervip',
            field=models.BooleanField(default=False),
        ),
    ]
