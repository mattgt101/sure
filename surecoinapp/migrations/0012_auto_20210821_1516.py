# Generated by Django 3.2.1 on 2021-08-21 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0011_auto_20210821_1333'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='payday',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='duration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
