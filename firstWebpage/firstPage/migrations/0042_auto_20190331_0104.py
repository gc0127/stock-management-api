# Generated by Django 2.0.7 on 2019-03-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0041_auto_20190331_0103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productlog',
            name='time',
            field=models.TimeField(default='01:04:18'),
        ),
        migrations.AlterField(
            model_name='products',
            name='order',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='rawmateriallog',
            name='time',
            field=models.TimeField(default='01:04:18'),
        ),
    ]
