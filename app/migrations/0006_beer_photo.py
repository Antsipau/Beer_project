# Generated by Django 3.1.4 on 2021-02-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20210203_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='beer',
            name='Photo',
            field=models.ImageField(default='', upload_to=''),
            preserve_default=False,
        ),
    ]
