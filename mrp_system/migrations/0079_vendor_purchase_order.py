# Generated by Django 2.1.2 on 2019-01-30 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0078_remove_purchaseorder_vendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor',
            name='purchase_order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='mrp_system.PurchaseOrder'),
        ),
    ]