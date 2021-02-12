# Generated by Django 3.1.4 on 2021-02-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20210203_1327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='characteristic',
            name='Gravity',
        ),
        migrations.AddField(
            model_name='characteristic',
            name='ABV',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='characteristic',
            name='OG',
            field=models.FloatField(default=0),
        ),
    ]
