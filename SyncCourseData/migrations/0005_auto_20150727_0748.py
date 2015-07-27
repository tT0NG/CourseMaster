# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0004_course_users_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='the_first',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='course',
            name='the_premium',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
