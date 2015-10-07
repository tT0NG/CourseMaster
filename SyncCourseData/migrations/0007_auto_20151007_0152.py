# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0006_auto_20150804_1154'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='users_ordered',
            new_name='user_list',
        ),
        migrations.RemoveField(
            model_name='classlog',
            name='count',
        ),
        migrations.RemoveField(
            model_name='course',
            name='the_first',
        ),
        migrations.RemoveField(
            model_name='course',
            name='the_premium',
        ),
        migrations.AddField(
            model_name='classlog',
            name='catchedcourse',
            field=models.TextField(default=b'[]'),
        ),
        migrations.AddField(
            model_name='classlog',
            name='failed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='classlog',
            name='failedcourse',
            field=models.TextField(default=b'[]'),
        ),
        migrations.AddField(
            model_name='classlog',
            name='success',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='course',
            name='super_vip_list',
            field=models.TextField(default=b'[]', null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='vip_list',
            field=models.TextField(default=b'[]', null=True),
        ),
    ]
