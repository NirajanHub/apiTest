# Generated by Django 2.2.5 on 2019-12-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, max_length=255, null=True, upload_to='pics')),
                ('category', models.CharField(max_length=2)),
            ],
        ),
    ]