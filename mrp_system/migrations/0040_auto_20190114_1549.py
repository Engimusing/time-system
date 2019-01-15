# Generated by Django 2.1.2 on 2019-01-14 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mrp_system', '0039_product_part_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAmount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(blank=True, default=1, null=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Amount',
            new_name='PartAmount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='part_products',
        ),
        migrations.AddField(
            model_name='productamount',
            name='from_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='source', to='mrp_system.Product'),
        ),
        migrations.AddField(
            model_name='productamount',
            name='to_product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mrp_system.Product'),
        ),
        migrations.AddField(
            model_name='product',
            name='component_product',
            field=models.ManyToManyField(through='mrp_system.ProductAmount', to='mrp_system.Product'),
        ),
    ]
