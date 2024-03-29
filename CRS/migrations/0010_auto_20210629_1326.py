# Generated by Django 3.2 on 2021-06-29 05:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0009_auto_20210628_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentscheduling',
            name='test',
            field=models.CharField(max_length=100, null=True, verbose_name='Room'),
        ),
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 5, 26, 1, 219990, tzinfo=utc)),
        ),
    ]
