# Generated by Django 2.0.7 on 2018-08-09 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstPage', '0012_auto_20180808_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rawmateriallog',
            name='item_name',
        ),
        migrations.AddField(
            model_name='rawmateriallog',
            name='item_id',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, to='firstPage.RawMaterial'),
            preserve_default=False,
        ),
    ]
