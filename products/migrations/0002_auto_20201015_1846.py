# Generated by Django 2.2 on 2020-10-15 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='ratings',
            field=models.ManyToManyField(blank=True, through='products.Rating', to='users.Customer'),
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Seller'),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('user', 'product')},
        ),
    ]
