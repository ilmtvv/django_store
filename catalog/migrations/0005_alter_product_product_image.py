# Generated by Django 4.2.7 on 2023-11-30 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/products', verbose_name='изображение продукта'),
        ),
    ]
