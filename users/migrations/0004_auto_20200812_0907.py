# Generated by Django 3.0.8 on 2020-08-12 03:37

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200811_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=stdimage.models.JPEGField(default='default.png', upload_to='profile_pics'),
        ),
    ]
