# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-10-26 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sicapp', '0007_userprofile_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='puesto',
            field=models.CharField(default='admin', max_length=50),
        ),
    ]
