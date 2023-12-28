from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    product_name = models.CharField(max_length=64, verbose_name='имя продукта')
    product_description = models.CharField(max_length=128, verbose_name='описание продукта')
    product_image = models.ImageField(upload_to='images/products', verbose_name='изображение продукта', **NULLABLE)
    product_category = models.ForeignKey('Category', on_delete=models.CASCADE, verbose_name='категория продукта')
    product_price = models.FloatField(max_length=64, verbose_name='цена продукта')
    data_of_creation = models.DateField(verbose_name='дата создания продукта')
    data_of_modified = models.DateField(verbose_name='дата последнего изменения')

    version = models.CharField(max_length=10, **NULLABLE)

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE)

class VersionProduct(models.Model):
    product_pk = models.ForeignKey('Product', on_delete=models.CASCADE, **NULLABLE)
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=False,)




class Category(models.Model):
    category_name = models.CharField(max_length=64, verbose_name='имя категории')
    category_description = models.CharField(max_length=128, verbose_name='описание категории')
    #created_at = models.CharField(max_length=4, verbose_name='test')

    def __str__(self):
        return self.category_name


class Contacts(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    message = models.CharField(max_length=10)


class BlogNotes(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, verbose_name='slug')
    content = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/blog', **NULLABLE)
    date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    views = models.IntegerField(default=0)
