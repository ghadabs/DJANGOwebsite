# Generated by Django 2.2.3 on 2019-08-26 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0011_auto_20190826_1340'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_fr',
            field=models.SlugField(max_length=200, null=True, unique=True, verbose_name='slug'),
        ),
    ]
