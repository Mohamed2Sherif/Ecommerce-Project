# Generated by Django 5.0.6 on 2024-06-07 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src_orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='delivered',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]