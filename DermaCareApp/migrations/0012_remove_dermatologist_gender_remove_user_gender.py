# Generated by Django 4.1.7 on 2023-03-31 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0011_remove_dermatologist_dermacv_file_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dermatologist',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='user',
            name='gender',
        ),
    ]
