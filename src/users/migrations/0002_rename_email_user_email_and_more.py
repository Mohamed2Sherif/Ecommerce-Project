# Generated by Django 5.0 on 2023-12-22 23:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("src_users", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user",
            old_name="Email",
            new_name="email",
        ),
        migrations.RenameField(
            model_name="user",
            old_name="User_Name",
            new_name="username",
        ),
    ]