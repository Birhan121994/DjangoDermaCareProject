# Generated by Django 4.1.7 on 2023-04-04 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0016_userprofile_first_name_userprofile_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='BlogPosts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogcomments', to='DermaCareApp.blogpost'),
        ),
    ]