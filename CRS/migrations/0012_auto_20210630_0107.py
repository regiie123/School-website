# Generated by Django 3.2.4 on 2021-06-29 17:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('CRS', '0011_auto_20210630_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hdapplicant',
            name='hd_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='loaapplicant',
            name='LOA_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='ojtapplicant',
            name='ojt_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='shifterapplicant',
            name='shifter_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='spapplicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transfereeapplicant',
            name='transfer_dateSubmitted',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 29, 17, 7, 38, 986407, tzinfo=utc)),
        ),
    ]
