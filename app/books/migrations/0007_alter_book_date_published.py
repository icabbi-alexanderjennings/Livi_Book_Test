# Generated by Django 4.2.7 on 2023-12-03 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_remove_author_first_name_remove_author_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date_published',
            field=models.DateField(),
        ),
    ]