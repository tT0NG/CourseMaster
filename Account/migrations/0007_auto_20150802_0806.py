# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0006_account_psu_is_set'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='psu_account',
            field=models.CharField(max_length=40),
        ),
    ]
