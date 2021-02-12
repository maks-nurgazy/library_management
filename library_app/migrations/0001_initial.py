# Generated by Django 3.1.6 on 2021-02-12 06:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('date_of_death', models.DateField(blank=True, default=None, null=True)),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
                'ordering': ['name', 'surname'],
                'get_latest_by': 'name',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('isbn', models.CharField(help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>', max_length=13, unique=True, verbose_name='ISBN')),
                ('year', models.PositiveSmallIntegerField(default=2021)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='BookProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_amount', models.IntegerField()),
                ('book_amount_total', models.IntegerField()),
                ('days_amount', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Book profile',
                'verbose_name_plural': 'Book profiles',
                'ordering': ['days_amount'],
                'get_latest_by': 'days_amount',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre (e.g. Science Fiction, French Poetry etc.)', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text="Enter the book's natural language (e.g. English, French, Japanese etc.)", max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
            ],
        ),
    ]
