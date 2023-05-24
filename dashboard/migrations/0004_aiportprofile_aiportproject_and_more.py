# Generated by Django 4.1.3 on 2023-04-24 23:42

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_aknowledge_create_by_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AiportProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airportuid', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('crit_aircraft', models.CharField(blank=True, max_length=200, null=True)),
                ('icao_code', models.CharField(blank=True, max_length=200, null=True)),
                ('designation', models.CharField(blank=True, max_length=200, null=True)),
                ('nehca', models.CharField(blank=True, max_length=200, null=True)),
                ('runway_dimension', models.CharField(blank=True, max_length=200, null=True)),
                ('runway_surface', models.CharField(blank=True, max_length=200, null=True)),
                ('runway_obstacles', models.CharField(blank=True, max_length=200, null=True)),
                ('runway_remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('taxiway_dimension', models.CharField(blank=True, max_length=200, null=True)),
                ('taxiway_surface', models.CharField(blank=True, max_length=200, null=True)),
                ('taxiway_num', models.IntegerField(blank=True, null=True)),
                ('taxiway_description', models.CharField(blank=True, max_length=200, null=True)),
                ('apron_dimension', models.CharField(blank=True, max_length=200, null=True)),
                ('apron_surface', models.CharField(blank=True, max_length=200, null=True)),
                ('apron_num', models.IntegerField(blank=True, null=True)),
                ('ptb_dimension', models.CharField(blank=True, max_length=200, null=True)),
                ('ptb_aircon', models.CharField(blank=True, max_length=200, null=True)),
                ('ptb_toilet', models.CharField(blank=True, max_length=200, null=True)),
                ('tower', models.CharField(blank=True, max_length=200, null=True)),
                ('com_flight', models.CharField(blank=True, max_length=200, null=True)),
                ('note', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AiportProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('fund_particulars', models.CharField(blank=True, max_length=200, null=True)),
                ('contract_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('profile', models.CharField(blank=True, max_length=200, null=True)),
                ('status_desc', models.CharField(blank=True, max_length=200, null=True)),
                ('slippage', models.CharField(blank=True, max_length=200, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=10)),
                ('agency', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(blank=True, max_length=200, null=True)),
                ('area', models.CharField(blank=True, max_length=200, null=True)),
                ('region', models.CharField(blank=True, max_length=200, null=True)),
                ('certificate', models.CharField(blank=True, max_length=200, null=True)),
                ('recouped_pay', models.CharField(blank=True, max_length=200, null=True)),
                ('progress', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='aknowledge',
            name='create_by_id',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]