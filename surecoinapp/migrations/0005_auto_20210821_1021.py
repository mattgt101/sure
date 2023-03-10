# Generated by Django 3.2.1 on 2021-08-21 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('surecoinapp', '0004_member_deposit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='active_deposit',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='balance',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='deposit',
            field=models.CharField(blank=True, default=0.0, max_length=200, null=True),
        ),
    ]
