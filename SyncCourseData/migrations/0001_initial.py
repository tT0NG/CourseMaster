# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_number', models.CharField(unique=True, max_length=100)),
                ('class_title', models.CharField(max_length=100)),
                ('class_code', models.CharField(max_length=100)),
                ('class_campus', models.CharField(max_length=100)),
                ('class_time', models.CharField(max_length=100, null=True)),
                ('is_active', models.BooleanField(default=False)),
                ('the_first', models.CharField(max_length=100)),
                ('the_premium', models.CharField(max_length=100)),
                ('users_ordered', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
