# Generated by Django 2.1.2 on 2019-01-30 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0077_purchaseorderparts_item_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='purchaseorder',
            name='vendor',
        ),
    ]