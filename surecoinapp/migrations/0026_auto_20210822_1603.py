# Generated by Django 3.2.1 on 2021-08-22 23:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0025_auto_20210822_1559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 16, 3, 56, 605175), null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='ref_bal',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
    ]