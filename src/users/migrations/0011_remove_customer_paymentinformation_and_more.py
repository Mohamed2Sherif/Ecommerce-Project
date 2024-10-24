# Generated by Django 5.0.6 on 2024-06-05 15:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("src_users", "0010_vendor_paymentinformation_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customer",
            name="paymentInformation",
        ),
        migrations.AddField(
            model_name="paymentinformation",
            name="payOnDelivery",
            field=models.BooleanField(blank=True, default=1, verbose_name="POD"),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name="Vendor",
        ),
    ]
