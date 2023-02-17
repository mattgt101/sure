# Generated by Django 3.2.1 on 2021-08-23 08:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0031_auto_20210822_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 23, 1, 51, 19, 17254), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='duration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 23, 1, 51, 19, 17254), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='payday',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 23, 1, 51, 19, 17254), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='profit',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
