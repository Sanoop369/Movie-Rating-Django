# Generated by Django 4.1.2 on 2022-11-08 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_review'),
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_date', models.DateField()),
            ],
        ),
    ]
