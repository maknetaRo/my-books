# Generated by Django 2.1.2 on 2018-10-27 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='book',
            new_name='post',
        ),
    ]