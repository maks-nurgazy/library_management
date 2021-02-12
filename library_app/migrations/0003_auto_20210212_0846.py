# Generated by Django 3.1.6 on 2021-02-12 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20210212_0653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200, unique=True),
        ),
    ]
