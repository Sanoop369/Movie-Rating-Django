# Generated by Django 4.1.2 on 2022-10-16 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genres',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=25)),
                ('dob', models.IntegerField()),
                ('contact', models.IntegerField()),
                ('email', models.CharField(max_length=25)),
                ('bio', models.CharField(max_length=200)),
                ('profile_img', models.ImageField(default='blank_profile.png', upload_to='profile_images')),
            ],
        ),
        migrations.CreateModel(
            name='User_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('user_type', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('lead_actor', models.CharField(max_length=100)),
                ('release_date', models.DateTimeField()),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.genres')),
            ],
        ),
    ]
