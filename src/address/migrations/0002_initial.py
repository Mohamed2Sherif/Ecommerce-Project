# Generated by Django 5.0 on 2024-02-04 00:23

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("src_address", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(fields=["user"], name="src_address_user_id_4f5b17_idx"),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(
                fields=["effective_date"], name="src_address_effecti_75c516_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(
                fields=["address_type"], name="src_address_address_2c8bf1_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(
                fields=["country"], name="src_address_country_dd2fd8_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="address",
            index=models.Index(
                fields=["zip_code"], name="src_address_zip_cod_76126d_idx"
            ),
        ),
    ]
