# Generated by Django 3.1 on 2021-07-06 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('inactive', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'timepiece_project',
                'ordering': ('name',),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='ProjectRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_relationships', to='manager.project')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='project_relationships', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'timepiece_projectrelationship',
                'default_permissions': (),
                'unique_together': {('user', 'project')},
            },
        ),
        migrations.AddField(
            model_name='project',
            name='users',
            field=models.ManyToManyField(related_name='user_projects', through='manager.ProjectRelationship', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(blank=True, default=' ', max_length=4)),
                ('title', models.CharField(blank=True, default=' ', max_length=20)),
                ('payroll', models.BooleanField(default=True)),
                ('health_insurance', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('payroll_name', models.CharField(blank=True, default='blahblahblah', max_length=20)),
                ('salaried', models.BooleanField(default=True)),
                ('hourly', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'manager_profile',
                'default_permissions': (),
            },
        ),
    ]
