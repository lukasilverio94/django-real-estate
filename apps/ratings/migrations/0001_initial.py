# Generated by Django 5.0.3 on 2024-04-01 14:57

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("profiles", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Rating",
            fields=[
                (
                    "pkid",
                    models.BigAutoField(
                        editable=False, primary_key=True, serialize=False
                    ),
                ),
                (
                    "id",
                    models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("update_at", models.DateTimeField(auto_now=True)),
                (
                    "rating",
                    models.IntegerField(
                        choices=[
                            (1, "Poor"),
                            (2, "Fair"),
                            (3, "Good"),
                            (4, "Very Good"),
                            (5, "Excellent"),
                        ],
                        default=0,
                        help_text="1=Poor, 2=Fair, 3=Good, 4=Very Good, 5=Excellent",
                        verbose_name="Rating",
                    ),
                ),
                ("comment", models.TextField(verbose_name="Comment")),
                (
                    "agent",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="agent_review",
                        to="profiles.profile",
                        verbose_name="Agent being rated",
                    ),
                ),
                (
                    "rater",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User providing the rating",
                    ),
                ),
            ],
            options={
                "unique_together": {("rater", "agent")},
            },
        ),
    ]