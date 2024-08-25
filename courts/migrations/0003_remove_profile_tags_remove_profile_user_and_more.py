# Generated by Django 5.0.6 on 2024-08-25 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0001_initial"),
        ("courts", "0002_court_description_court_is_available_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="profile",
            name="tags",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="user",
        ),
        migrations.RemoveField(
            model_name="trainer",
            name="profile",
        ),
        migrations.RemoveField(
            model_name="user",
            name="groups",
        ),
        migrations.RemoveField(
            model_name="user",
            name="user_permissions",
        ),
        migrations.AlterField(
            model_name="reservation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="accounts.user"
            ),
        ),
        migrations.AlterField(
            model_name="reservation",
            name="type",
            field=models.CharField(
                choices=[
                    ("regular", "Zwykła"),
                    ("league", "Liga Format"),
                    ("school", "Trening"),
                    ("membership", "ClubCard"),
                ],
                max_length=50,
            ),
        ),
        migrations.DeleteModel(
            name="Tag",
        ),
        migrations.DeleteModel(
            name="Profile",
        ),
        migrations.DeleteModel(
            name="Trainer",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]
