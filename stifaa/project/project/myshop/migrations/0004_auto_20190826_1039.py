# Generated by Django 2.2.3 on 2019-08-26 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0003_auto_20190823_1217'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_fr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_fr',
        ),
    ]
