# Generated by Django 2.1.2 on 2018-12-27 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0025_auto_20181226_1736'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='prefix',
            field=models.CharField(max_length=5),
        ),
    ]
