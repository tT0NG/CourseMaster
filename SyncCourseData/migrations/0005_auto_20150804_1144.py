# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0004_classlog_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='the_first',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='the_premium',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
