# Generated by Django 2.2.20 on 2021-05-05 04:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 4, 35, 55, 320660, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='summary',
            name='defence_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 5, 4, 35, 55, 330549, tzinfo=utc)),
        ),
    ]