# Generated by Django 5.1.1 on 2024-09-29 07:06

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="UserInfo",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("streak", models.IntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.AddField(
            model_name="user",
            name="user_info",
            field=models.OneToOneField(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="users.userinfo",
            ),
            preserve_default=False,
        ),
    ]
