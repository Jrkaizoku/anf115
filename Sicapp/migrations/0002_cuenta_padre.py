# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-02 17:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sicapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuenta',
            name='padre',
            field=models.BooleanField(default=False),
        ),
    ]
