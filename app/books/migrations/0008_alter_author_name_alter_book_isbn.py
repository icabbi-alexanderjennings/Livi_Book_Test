# Generated by Django 4.2.7 on 2023-12-03 21:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_date_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='', max_length=20, validators=[django.core.validators.RegexValidator(message='Please enter a valid ISDN', regex='^(?=(?:\\D*\\d){10}(?:(?:\\D*\\d){3})?$)[\\d-]+$')]),
        ),
    ]