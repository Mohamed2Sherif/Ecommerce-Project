# Generated by Django 4.2.10 on 2024-02-22 23:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("src_users", "0005_alter_otp_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="otp",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
