# Generated by Django 2.2.5 on 2019-12-07 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memesimages', '0003_auto_20191205_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memesimages',
            name='images',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='pics/%Y/%m/%d'),
        ),
    ]