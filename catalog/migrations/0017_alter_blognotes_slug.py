# Generated by Django 4.2.7 on 2023-12-08 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0016_alter_blognotes_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognotes',
            name='slug',
            field=models.CharField(max_length=100, verbose_name='slug'),
        ),
    ]
