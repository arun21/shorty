# Generated by Django 3.1.1 on 2020-09-16 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='short_urls',
            name='comment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='short_urls',
            name='long_url',
            field=models.URLField(unique=True, verbose_name='Enter URL '),
        ),
        migrations.AlterField(
            model_name='short_urls',
            name='short_url',
            field=models.CharField(max_length=20),
        ),
    ]
