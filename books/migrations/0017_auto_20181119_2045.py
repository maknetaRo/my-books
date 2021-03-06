# Generated by Django 2.1.2 on 2018-11-19 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_auto_20181119_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Podaj gatuenk książki', max_length=200),
        ),
    ]
