# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-29 17:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visiter', '0003_auto_20170928_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
