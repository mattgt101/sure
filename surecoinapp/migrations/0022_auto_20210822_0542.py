# Generated by Django 3.2.1 on 2021-08-22 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0021_auto_20210822_0300'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='pin',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 5, 42, 24, 472466), null=True),
        ),
    ]
