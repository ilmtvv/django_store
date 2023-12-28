# Generated by Django 4.2.7 on 2023-12-05 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogNotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/blog')),
                ('date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('views', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
