# Generated by Django 4.1.7 on 2023-06-11 19:51

import DermaCareApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0035_alter_appointment_email_alter_appointment_phone_no_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='derma_user',
            field=models.CharField(default='', max_length=50, validators=[DermaCareApp.models.check_valid_derma]),
        ),
    ]
