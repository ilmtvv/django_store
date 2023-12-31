# Generated by Django 4.2.7 on 2023-12-23 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_alter_blognotes_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('is_active', models.BooleanField(default=False, unique=True)),
                ('product_pk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.product')),
            ],
        ),
    ]
