# Generated by Django 4.2.7 on 2023-11-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_remove_produtovenda_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtovenda',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
