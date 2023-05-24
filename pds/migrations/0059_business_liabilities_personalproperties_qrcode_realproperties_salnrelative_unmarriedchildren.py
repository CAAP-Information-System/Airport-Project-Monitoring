# Generated by Django 3.2.8 on 2022-12-27 03:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pds', '0058_remove_bonuses_total_year_end_bonus'),
    ]

    operations = [
        migrations.CreateModel(
            name='UnmarriedChildren',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='birth')),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('child', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_child', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalnRelative',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('relationship', models.CharField(blank=True, max_length=200, null=True)),
                ('position', models.CharField(blank=True, max_length=200, null=True)),
                ('agency', models.CharField(blank=True, max_length=200, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('relative', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_relative', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RealProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('kind', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=200, null=True)),
                ('assesed_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('market_value', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('aquired_year', models.CharField(blank=True, max_length=200, null=True)),
                ('aquired_mode', models.CharField(blank=True, max_length=200, null=True)),
                ('aquired_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('real_properties', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_real', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Qrcode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url_name', models.CharField(blank=True, max_length=200, null=True)),
                ('emp_name', models.CharField(blank=True, max_length=200, null=True)),
                ('unique_id', models.CharField(blank=True, max_length=200, null=True)),
                ('qr_code', models.ImageField(blank=True, upload_to='qr_codes')),
                ('qr', models.ForeignKey(blank=True, db_column='personal_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_qr', to='pds.personal')),
            ],
        ),
        migrations.CreateModel(
            name='PersonalProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('aquired_year', models.CharField(blank=True, max_length=200, null=True)),
                ('aquired_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('personal_properties', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_personal', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Liabilities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nature', models.CharField(blank=True, max_length=200, null=True)),
                ('creditor', models.CharField(blank=True, max_length=200, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('liabilities', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_liabilities', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entity_business', models.CharField(blank=True, max_length=200, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('nature', models.CharField(blank=True, max_length=200, null=True)),
                ('date_aquired', models.CharField(blank=True, max_length=100, null=True)),
                ('edited_by', models.CharField(blank=True, max_length=100, null=True)),
                ('date_created', models.DateField(blank=True, null=True, verbose_name='created_date')),
                ('business', models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='saln_business', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]