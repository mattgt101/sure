# Generated by Django 3.2.1 on 2021-08-22 21:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0023_auto_20210822_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='ref_bal',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 14, 59, 56, 497331), null=True),
        ),
    ]
