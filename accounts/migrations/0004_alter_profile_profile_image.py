# Generated by Django 5.0.6 on 2024-08-26 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0003_alter_profile_user_remove_profile_location_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="profile_image",
            field=models.ImageField(
                blank=True, default="profiles/tenis_17.png", upload_to="profiles/"
            ),
        ),
    ]
