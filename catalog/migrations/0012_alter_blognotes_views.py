# Generated by Django 4.2.7 on 2023-12-08 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_alter_blognotes_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognotes',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]