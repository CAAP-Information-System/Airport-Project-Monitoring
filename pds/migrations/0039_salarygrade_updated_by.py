# Generated by Django 3.2.8 on 2022-09-19 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0038_signatory_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='salarygrade',
            name='updated_by',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]