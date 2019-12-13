# Generated by Django 2.2.5 on 2019-12-10 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadImage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=2)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
