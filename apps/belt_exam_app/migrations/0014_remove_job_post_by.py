# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-21 03:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0013_job_post_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='post_by',
        ),
    ]
