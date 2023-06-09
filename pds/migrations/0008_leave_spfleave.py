# Generated by Django 3.2.8 on 2022-06-23 05:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0007_auto_20220623_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='SPFLeave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('force', models.CharField(max_length=200)),
                ('special', models.CharField(max_length=200)),
                ('leave', models.ForeignKey(blank=True, db_column='personal_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pds_spfleave', to='pds.personal')),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period', models.DateField(blank=True, null=True, verbose_name='period')),
                ('particulars', models.CharField(max_length=200)),
                ('vacation_earned', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('vacation_wpay', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('vacation_wopay', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('vacation_balance', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('sick_earned', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('sick_wpay', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('sick_wopay', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('sick_balance', models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True)),
                ('remarks', models.CharField(max_length=200)),
                ('leave', models.ForeignKey(blank=True, db_column='personal_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pds_leave', to='pds.personal')),
            ],
        ),
    ]
