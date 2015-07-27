# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_account_courses_caught'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='psu_account',
            field=models.CharField(default=b'123', max_length=40),
        ),
        migrations.AddField(
            model_name='account',
            name='psu_password',
            field=models.CharField(default=b'123', max_length=100),
        ),
    ]
