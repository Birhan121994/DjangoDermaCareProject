# Generated by Django 4.1.7 on 2023-03-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0004_user_location_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(default='Default Value', max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(default='Default Value', max_length=50),
        ),
    ]
