# Generated by Django 4.1.2 on 2022-11-17 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opticalcrm', '0002_invoice_totalpurch'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice_products',
            name='pprice',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]