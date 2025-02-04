# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-08-08 17:48
from django.db import migrations
from django.db import OperationalError


def set_location_type(apps, schema_editor):
    try:
        NetworkLocation = apps.get_model("discovery", "NetworkLocation")
        NetworkLocation.objects.filter(dynamic=True).update(location_type="dynamic")
        NetworkLocation.objects.filter(dynamic=False).update(location_type="static")
    except OperationalError as e:
        # if running migrations from scratch, the table may not exist yet
        if "no such table: discovery_networklocation" in str(e):
            return


def revert_location_type(apps, schema_editor):
    try:
        NetworkLocation = apps.get_model("discovery", "NetworkLocation")
        NetworkLocation.objects.filter(location_type="dynamic").update(dynamic=True)
        NetworkLocation.objects.filter(location_type="static").update(dynamic=False)
    except OperationalError as e:
        # if running migrations from scratch, the table may not exist yet
        if "no such table: discovery_networklocation" in str(e):
            return


class Migration(migrations.Migration):

    dependencies = [
        ("discovery", "0009_add_location_type"),
    ]

    operations = [
        migrations.RunPython(
            set_location_type,
            reverse_code=revert_location_type,
            # make sure NetworkLocationRouter routes this migration to the correct database
            hints={"model_name": "networklocation"},
        )
    ]
