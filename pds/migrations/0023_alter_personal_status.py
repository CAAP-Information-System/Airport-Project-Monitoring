# Generated by Django 3.2.8 on 2022-08-03 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0022_personal_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal',
            name='status',
            field=models.CharField(blank=True, default='For Approval', max_length=200, null=True),
        ),
    ]
