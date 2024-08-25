# Generated by Django 5.0.6 on 2024-08-25 16:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_remove_profile_balance_of_hours_profile_city_and_more"),
        ("courts", "0004_alter_reservation_user"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.RemoveField(
            model_name="profile",
            name="location",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="social_facebook",
        ),
        migrations.RemoveField(
            model_name="profile",
            name="social_twitter",
        ),
        migrations.DeleteModel(
            name="User",
        ),
    ]