# Generated by Django 3.2.8 on 2022-06-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0009_auto_20220623_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='created'),
        ),
    ]
