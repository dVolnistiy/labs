# Generated by Django 3.1.2 on 2021-12-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_room', models.IntegerField(help_text='Enter the number of room in which you want check PC')),
                ('floor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.floor')),
            ],
        ),
    ]
