# Generated by Django 4.1.3 on 2022-12-04 11:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_watchlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watchlist',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
