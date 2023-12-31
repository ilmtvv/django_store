from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='имя продукта')
    product_description = models.CharField(max_length=128, verbose_name='описание продукта')
    product_image = models.ImageField(upload_to='images/products', verbose_name='изображение продукта', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория продукта')
    product_price = models.FloatField(max_length=64, verbose_name='цена продукта')
    data_of_creation = models.DateField(verbose_name='дата создания продукта')
    data_of_modified = models.DateField(verbose_name='дата последнего изменения')


class Category(models.Model):
    category_name = models.CharField(max_length=64, verbose_name='имя категории')
    category_description = models.CharField(max_length=128, verbose_name='описание категории')
    #created_at = models.CharField(max_length=4, verbose_name='test')

    def __str__(self):
        return self.category_name

