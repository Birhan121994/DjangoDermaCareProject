# Generated by Django 4.1.7 on 2023-04-07 23:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DermaCareApp', '0021_alter_blogcomment_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='reply',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
