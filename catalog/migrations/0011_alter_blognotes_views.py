# Generated by Django 4.2.7 on 2023-12-08 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_blognotes_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blognotes',
            name='views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
