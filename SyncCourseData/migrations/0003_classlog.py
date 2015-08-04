# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SyncCourseData', '0002_auto_20150803_0914'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('running', models.BooleanField(default=False)),
            ],
        ),
    ]
