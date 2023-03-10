# Generated by Django 3.2.1 on 2021-08-23 09:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0032_auto_20210823_0151'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 23, 2, 11, 9, 655163), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 23, 2, 11, 9, 654167), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='duration',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 23, 2, 11, 9, 654167), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='payday',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 8, 23, 2, 11, 9, 654167), null=True),
        ),
    ]
