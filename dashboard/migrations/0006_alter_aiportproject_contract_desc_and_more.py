# Generated by Django 4.1.3 on 2023-05-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_alter_aiportproject_contract_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aiportproject',
            name='contract_desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='description',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='fund_particulars',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='profile',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='status',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='aiportproject',
            name='status_desc',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
