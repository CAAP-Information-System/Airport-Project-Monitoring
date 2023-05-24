# Generated by Django 4.1.3 on 2023-03-28 08:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pds', '0062_multipleimage_caapeu'),
    ]

    operations = [
        migrations.AddField(
            model_name='multipleimage',
            name='post',
            field=models.ForeignKey(blank=True, db_column='post_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_up', to='pds.post'),
        ),
       
    ]
