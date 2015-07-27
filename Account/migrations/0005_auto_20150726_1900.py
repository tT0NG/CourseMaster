# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0004_auto_20150726_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='psu_account',
            field=models.CharField(unique=True, max_length=40),
        ),
        migrations.AlterField(
            model_name='account',
            name='psu_password',
            field=models.CharField(max_length=100),
        ),
    ]
