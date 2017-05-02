# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-02 21:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginReg', '0001_initial'),
        ('thor', '0003_trip_travelers'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='planner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator', to='loginReg.User'),
            preserve_default=False,
        ),
    ]
