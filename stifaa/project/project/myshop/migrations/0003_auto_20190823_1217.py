# Generated by Django 2.2.3 on 2019-08-23 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20190823_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug_en',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='category',
            name='slug_fr',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]
