# Generated by Django 2.2.3 on 2019-08-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='new_price',
            new_name='newprice',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='old_price',
            new_name='oldprice',
        ),
    ]
