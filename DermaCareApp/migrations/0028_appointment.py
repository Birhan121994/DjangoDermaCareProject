# Generated by Django 4.1.7 on 2023-05-10 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0027_rename_reply_content_reply_reply_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_no', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('prefered_date_time', models.DateTimeField(null=True)),
                ('request', models.TextField(blank=True)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('accepted', models.BooleanField(default=False, verbose_name='Approve')),
                ('rejected', models.BooleanField(default=False, verbose_name='Reject')),
            ],
            options={
                'ordering': ['-sent_date'],
            },
        ),
    ]