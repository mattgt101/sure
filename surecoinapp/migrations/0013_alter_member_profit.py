# Generated by Django 3.2.1 on 2021-08-21 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0012_auto_20210821_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='profit',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
