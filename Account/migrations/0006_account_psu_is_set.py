# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20150726_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='psu_is_set',
            field=models.BooleanField(default=False),
        ),
    ]
