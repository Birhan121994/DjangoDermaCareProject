# Generated by Django 4.1.7 on 2023-05-10 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0029_dermacategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='derma_user',
            field=models.CharField(default='dermauser', max_length=50),
        ),
    ]
