# Generated by Django 2.1.2 on 2019-01-30 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0065_purchaseorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manufacturer',
            new_name='Vendor',
        ),
    ]