# Generated by Django 4.1.2 on 2022-11-06 05:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_remove_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(help_text='write your commet')),
                ('comment_date', models.DateTimeField(auto_now_add=True)),
                ('time', models.DateField(default=datetime.datetime.now)),
                ('Movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.movies')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
