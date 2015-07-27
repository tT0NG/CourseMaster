# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_auto_20150715_0625'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='courses_caught',
            field=models.IntegerField(default=0),
        ),
    ]
