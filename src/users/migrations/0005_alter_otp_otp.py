# Generated by Django 4.2.10 on 2024-02-22 21:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("src_users", "0004_alter_otp_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otp",
            name="otp",
            field=models.CharField(),
        ),
    ]
