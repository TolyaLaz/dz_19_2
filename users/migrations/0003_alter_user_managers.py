# Generated by Django 4.2.2 on 2024-08-28 18:20

from django.db import migrations
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_token"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", users.models.CustomUserManager()),
            ],
        ),
    ]
