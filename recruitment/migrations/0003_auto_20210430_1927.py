# Generated by Django 2.2.20 on 2021-04-30 13:57

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20210430_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 30, 13, 57, 18, 253701, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='defence_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 30, 13, 57, 18, 263279, tzinfo=utc)),
        ),
    ]
