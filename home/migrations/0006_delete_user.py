# Generated by Django 4.1.2 on 2022-10-20 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_user_delete_user_details_delete_user_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
