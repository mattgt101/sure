# Generated by Django 3.2.1 on 2021-08-22 23:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0027_auto_20210822_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 16, 43, 9, 636583), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='l_withraw',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='t_profit',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='t_withdraw',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
    ]
