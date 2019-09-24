# Generated by Django 2.2.3 on 2019-08-20 08:06

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('img', models.ImageField(blank=True, upload_to='images/')),
                ('subcategories', multiselectfield.db.fields.MultiSelectField(choices=[('sub1', 'sub1'), ('sub2', 'sub2'), ('sub3', 'sub3'), ('sub4', 'sub4'), ('sub5', 'sub5')], max_length=1000)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory', models.CharField(choices=[('sub1', 'sub1'), ('sub2', 'sub2'), ('sub3', 'sub3'), ('sub4', 'sub4'), ('sub5', 'sub5')], max_length=1000)),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('img1', models.ImageField(blank=True, upload_to='images/')),
                ('img2', models.ImageField(blank=True, upload_to='images/')),
                ('img3', models.ImageField(blank=True, upload_to='images/')),
                ('img4', models.ImageField(blank=True, upload_to='images/')),
                ('description', models.TextField(blank=True)),
                ('old_price', models.DecimalField(decimal_places=3, max_digits=1000)),
                ('new_price', models.DecimalField(decimal_places=3, max_digits=1000)),
                ('brand_photo', models.ImageField(blank=True, upload_to='images/')),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Product', to='sales.Category')),
            ],
            options={
                'ordering': ('-created',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
