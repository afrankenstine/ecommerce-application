# Generated by Django 2.2 on 2020-10-15 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20201015_1846'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='status',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='status',
            field=models.CharField(choices=[('paid', 'paid'), ('unpaid', 'unpaid')], default='unpaid', max_length=15),
        ),
        migrations.AddField(
            model_name='wishlistitems',
            name='status',
            field=models.CharField(choices=[('purchased', 'purchased'), ('remaining', 'remaining')], default='remaining', max_length=15),
        ),
    ]
