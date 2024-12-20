# Generated by Django 5.1.3 on 2024-12-04 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255, unique=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('brand', models.CharField(blank=True, max_length=255, null=True)),
                ('model_number', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('floor_no', models.IntegerField(blank=True, null=True)),
                ('line_no', models.IntegerField(blank=True, null=True)),
                ('supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('purchase_date', models.DateField(blank=True, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('last_breakdown_start', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('maintenance', 'Under Maintenance'), ('broken', 'Broken')], default='active', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Mechanic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BreakdownLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_category', models.CharField(max_length=255)),
                ('breakdown_start', models.DateTimeField()),
                ('lost_time', models.DurationField()),
                ('comments', models.TextField(blank=True, null=True)),
                ('operator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakdowns', to='user_management.employee')),
                ('machine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='breakdowns', to='maintenance.machine')),
                ('mechanic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='breakdowns', to='maintenance.mechanic')),
            ],
            options={
                'verbose_name': 'Breakdown Log',
                'verbose_name_plural': 'Breakdown Logs',
                'ordering': ['-breakdown_start'],
            },
        ),
    ]
