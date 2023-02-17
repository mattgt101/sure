# Generated by Django 3.2.1 on 2021-08-22 09:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0019_auto_20210821_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=type, max_length=200, null=True)),
                ('type', models.CharField(blank=type, max_length=200, null=True)),
                ('amount', models.CharField(blank=models.CharField(blank=type, max_length=200, null=True), max_length=200, null=True)),
                ('his_date', models.CharField(blank=models.CharField(blank=type, max_length=200, null=True), max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='member',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 8, 22, 2, 50, 34, 298809), null=True),
        ),
    ]
