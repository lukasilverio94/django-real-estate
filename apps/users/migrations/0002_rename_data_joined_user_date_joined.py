# Generated by Django 5.0.3 on 2024-04-01 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="data_joined",
            new_name="date_joined",
        ),
    ]