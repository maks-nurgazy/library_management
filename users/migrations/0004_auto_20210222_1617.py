# Generated by Django 3.1.6 on 2021-02-22 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_delete_adminmore'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=[('ADMIN', 'Admin'), ('LIBRARIAN', 'Librarian'), ('CUSTOMER', 'Customer')], default='ADMIN', max_length=20, null=True),
        ),
    ]
