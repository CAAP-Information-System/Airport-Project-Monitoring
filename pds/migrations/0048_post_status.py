# Generated by Django 3.2.8 on 2022-09-30 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pds', '0047_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]