# Generated by Django 4.2.7 on 2023-12-23 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_alter_versionproduct_product_pk'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='version',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
