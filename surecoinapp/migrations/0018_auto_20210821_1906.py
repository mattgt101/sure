# Generated by Django 3.2.1 on 2021-08-22 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0017_auto_20210821_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='t_withdraw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 21, 19, 6, 39, 807651), null=True),
        ),
    ]
