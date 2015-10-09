# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20151007_0358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_active',
            new_name='is_correct',
        ),
    ]
