# Generated by Django 3.2.8 on 2022-09-29 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0042_auto_20220923_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='position_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
