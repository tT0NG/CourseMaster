# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='courses_caught_list',
            field=models.TextField(default=b'[]'),
        ),
        migrations.AddField(
            model_name='account',
            name='courses_list',
            field=models.TextField(default=b'[]'),
        ),
    ]
