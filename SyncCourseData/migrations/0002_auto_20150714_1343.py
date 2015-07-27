# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='class_time',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='class_title',
            field=models.CharField(max_length=100),
        ),
    ]
