# Generated by Django 3.2.8 on 2022-11-28 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0056_auto_20221123_0852'),
    ]

    operations = [
        migrations.AddField(
            model_name='bonuses',
            name='total_year_end_bonus',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]