# Generated by Django 2.2.3 on 2019-08-27 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0013_auto_20190827_0828'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='slug_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='slug_fr',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategories_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='subcategories_fr',
        ),
        migrations.AddField(
            model_name='product',
            name='category_en',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='myshop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category_fr',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='myshop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_en',
            field=models.CharField(choices=[('sub1', 'sub1'), ('sub2', 'sub2'), ('sub3', 'sub3'), ('sub4', 'sub4'), ('sub5', 'sub5')], max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory_fr',
            field=models.CharField(choices=[('sub1', 'sub1'), ('sub2', 'sub2'), ('sub3', 'sub3'), ('sub4', 'sub4'), ('sub5', 'sub5')], max_length=1000, null=True),
        ),
    ]
