# Generated by Django 2.1.2 on 2019-01-21 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0052_auto_20190121_0916'),
    ]

    operations = [
        migrations.AddField(
            model_name='manufacturingorder',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2019, 1, 21, 19, 30, 46, 473514)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='manufacturingorder',
            name='number',
            field=models.CharField(default='2019-01-20 15:00:00', max_length=50),
            preserve_default=False,
        ),
    ]