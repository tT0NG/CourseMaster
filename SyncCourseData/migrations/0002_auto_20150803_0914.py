# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users_ordered',
        ),
        migrations.AddField(
            model_name='course',
            name='users_ordered',
            field=models.TextField(default=b'[]', null=True),
        ),
    ]
