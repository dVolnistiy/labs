# Generated by Django 4.0 on 2021-12-16 02:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_rename_number_of_floor_floor_floor_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workplace',
            old_name='place',
            new_name='places',
        ),
    ]