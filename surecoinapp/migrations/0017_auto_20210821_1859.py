# Generated by Django 3.2.1 on 2021-08-22 01:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0016_alter_member_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='l_withraw',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='t_profit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 21, 18, 59, 17, 958568), null=True),
        ),
    ]
