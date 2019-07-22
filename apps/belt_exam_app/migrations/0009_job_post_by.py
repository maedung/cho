# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-07-21 03:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belt_exam_app', '0008_remove_job_post_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='post_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posted', to='belt_exam_app.User'),
            preserve_default=False,
        ),
    ]
