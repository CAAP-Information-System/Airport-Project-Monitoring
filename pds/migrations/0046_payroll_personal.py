# Generated by Django 3.2.8 on 2022-09-30 03:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0045_remove_payroll_personal'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='personal',
            field=models.OneToOneField(blank=True, db_column='personal_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pds_personal', to='pds.personal'),
        ),
    ]
