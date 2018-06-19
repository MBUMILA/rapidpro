# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-06-15 20:40
from __future__ import unicode_literals

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("campaigns", "0024_add_fired_index")]

    operations = [
        migrations.AlterField(
            model_name="campaign",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="campaigns_campaign_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="group",
            field=models.ForeignKey(
                help_text="The group this campaign operates on",
                on_delete=django.db.models.deletion.PROTECT,
                to="contacts.ContactGroup",
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="campaigns_campaign_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="campaign",
            name="org",
            field=models.ForeignKey(
                help_text="The organization this campaign exists for",
                on_delete=django.db.models.deletion.PROTECT,
                to="orgs.Org",
            ),
        ),
        migrations.AlterField(
            model_name="campaignevent",
            name="created_by",
            field=models.ForeignKey(
                help_text="The user which originally created this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="campaigns_campaignevent_creations",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="campaignevent",
            name="modified_by",
            field=models.ForeignKey(
                help_text="The user which last modified this item",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="campaigns_campaignevent_modifications",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]