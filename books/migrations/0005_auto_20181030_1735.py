# Generated by Django 2.1.2 on 2018-10-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20181027_2004'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Podaj język w jakim napisana jest książka', max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='active',
            new_name='approved_comment',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='updated',
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ManyToManyField(to='books.Language'),
        ),
    ]
