# Generated by Django 4.1.2 on 2022-11-21 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opticalcrm', '0006_alter_invoice_pendingamount'),
    ]

    operations = [
        migrations.AddField(
            model_name='glass',
            name='barcode',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]