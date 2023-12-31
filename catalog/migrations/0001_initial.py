# Generated by Django 4.2.7 on 2023-11-20 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64, verbose_name='имя категории')),
                ('category_description', models.CharField(max_length=128, verbose_name='описание категории')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=64, verbose_name='имя продукта')),
                ('product_description', models.CharField(max_length=128, verbose_name='описание продукта')),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='изображение продукта')),
                ('product_price', models.FloatField(max_length=64, verbose_name='цена продукта')),
                ('data_of_creation', models.DateField(verbose_name='дата создания продукта')),
                ('data_of_modified', models.DateField(verbose_name='дата последнего изменения')),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.category', verbose_name='категория продукта')),
            ],
        ),
    ]
