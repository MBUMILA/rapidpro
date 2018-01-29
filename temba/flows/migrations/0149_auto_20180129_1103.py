# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-01-29 11:03
from __future__ import unicode_literals

from django.db import migrations
import temba.utils.models


class Migration(migrations.Migration):

    dependencies = [
        ('flows', '0148_auto_20180128_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flowrun',
            name='path',
            field=temba.utils.models.JSONAsTextField(help_text='The path taken during this flow run in JSON format', null=True),
        ),
    ]
