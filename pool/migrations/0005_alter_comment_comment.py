# Generated by Django 4.0.4 on 2022-06-08 02:28

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('pool', '0004_comment_image_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=tinymce.models.HTMLField(),
        ),
    ]
