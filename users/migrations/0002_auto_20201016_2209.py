# Generated by Django 2.2 on 2020-10-16 16:24

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='display_picture',
            field=models.FileField(blank=True, default='', upload_to=users.models.upload_dp_to),
        ),
    ]