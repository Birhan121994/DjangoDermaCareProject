# Generated by Django 4.1.7 on 2023-04-02 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0015_dermatologist_agree_dermatologist_gender_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='quotes',
            field=models.CharField(default='', max_length=100),
        ),
    ]