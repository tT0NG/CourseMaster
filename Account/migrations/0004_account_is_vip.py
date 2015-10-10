# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_auto_20151007_0152'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_vip',
            field=models.BooleanField(default=False),
        ),
    ]
