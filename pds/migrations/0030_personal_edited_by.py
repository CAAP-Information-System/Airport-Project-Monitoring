# Generated by Django 3.2.8 on 2022-08-09 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0029_auto_20220805_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal',
            name='edited_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
