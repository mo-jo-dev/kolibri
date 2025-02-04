# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-04-04 16:00
import django.db.models.deletion
import morango.models.fields.uuids
from django.db import migrations
from django.db import models

import kolibri.core.content.models
import kolibri.core.fields
import kolibri.utils.time_utils


class Migration(migrations.Migration):

    dependencies = [
        ("kolibriauth", "0023_change_extra_fields_validator"),
        ("content", "0032_contentnode_admin_imported"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContentRequest",
            fields=[
                (
                    "id",
                    morango.models.fields.uuids.UUIDField(
                        default=kolibri.core.content.models._hex_uuid_str,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("source_model", models.CharField(max_length=40)),
                ("source_id", morango.models.fields.uuids.UUIDField()),
                (
                    "requested_at",
                    kolibri.core.fields.DateTimeTzField(
                        default=kolibri.utils.time_utils.local_now
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("DOWNLOAD", "Download"), ("REMOVAL", "Removal")],
                        max_length=8,
                    ),
                ),
                (
                    "reason",
                    models.CharField(
                        choices=[
                            ("SYNC_INITIATED", "SyncInitiated"),
                            ("USER_INITIATED", "UserInitiated"),
                        ],
                        max_length=14,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("COMPLETED", "Completed"),
                            ("FAILED", "Failed"),
                            ("IN_PROGRESS", "InProgress"),
                            ("PENDING", "Pending"),
                        ],
                        max_length=11,
                    ),
                ),
                ("contentnode_id", morango.models.fields.uuids.UUIDField()),
                ("metadata", kolibri.core.fields.JSONField(null=True)),
                (
                    "facility",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="content_requests",
                        to="kolibriauth.Facility",
                    ),
                ),
            ],
            options={
                "ordering": ("requested_at",),
            },
        ),
        migrations.CreateModel(
            name="ContentDownloadRequest",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
            },
            bases=("content.contentrequest",),
        ),
        migrations.CreateModel(
            name="ContentRemovalRequest",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
            },
            bases=("content.contentrequest",),
        ),
        migrations.AlterUniqueTogether(
            name="contentrequest",
            unique_together=set(
                [("type", "source_model", "source_id", "contentnode_id")]
            ),
        ),
    ]
