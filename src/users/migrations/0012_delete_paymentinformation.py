# Generated by Django 5.0.6 on 2024-06-06 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src_users', '0011_remove_customer_paymentinformation_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PaymentInformation',
        ),
    ]