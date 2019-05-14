# Generated by Django 2.1.2 on 2019-05-13 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0009_auto_20190405_1156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('-start_time',), 'permissions': (('can_clock_in_out', 'Can use Pendulum to clock in and out'),), 'verbose_name_plural': 'entries'},
        ),
        migrations.AlterModelOptions(
            name='projecthours',
            options={'permissions': (('modify_admin_site', 'Can modify, add, or delete project hours'),), 'verbose_name': 'project hours entry', 'verbose_name_plural': 'project hours entries'},
        ),
    ]
