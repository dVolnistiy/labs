# Generated by Django 4.0 on 2021-12-16 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0009_room_building_alter_floor_building_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floor',
            old_name='number_of_floor',
            new_name='floor',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number_of_room',
            new_name='room_number',
        ),
    ]