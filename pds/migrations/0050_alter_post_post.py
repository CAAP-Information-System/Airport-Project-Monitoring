# Generated by Django 3.2.8 on 2022-09-30 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0049_rename_updated_by_post_create_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post',
            field=models.CharField(blank=True, max_length=800, null=True),
        ),
    ]
