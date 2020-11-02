# Generated by Django 2.1.2 on 2020-10-27 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_remove_profile_health_insurance'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='health_insurance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
            preserve_default=False,
        ),
    ]
