# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_number', models.CharField(unique=True, max_length=100)),
                ('class_title', models.CharField(max_length=200)),
                ('class_code', models.CharField(max_length=100)),
                ('class_campus', models.CharField(max_length=100)),
            ],
        ),
    ]
