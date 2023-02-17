# Generated by Django 3.2.1 on 2021-08-22 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0022_auto_20210822_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=type, max_length=200, null=True)),
                ('invited', models.CharField(blank=type, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='ref',
            field=models.CharField(blank=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='active_deposit',
            field=models.IntegerField(blank=True, default=0.0, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 12, 26, 41, 913938), null=True),
        ),
    ]