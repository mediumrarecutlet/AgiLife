# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20161031_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupevent',
            name='timeEnd',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='groupevent',
            name='timeStart',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='timeEnd',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='userevent',
            name='timeStart',
            field=models.DateTimeField(),
        ),
    ]
