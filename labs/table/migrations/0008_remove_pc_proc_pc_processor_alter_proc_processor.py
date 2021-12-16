# Generated by Django 4.0 on 2021-12-15 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_auto_20211215_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pc',
            name='proc',
        ),
        migrations.AddField(
            model_name='pc',
            name='processor',
            field=models.CharField(choices=[('AMD_Ryzen_5000', 'Ryzen 5000')], max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='proc',
            name='processor',
            field=models.CharField(choices=[('AMD_Ryzen_5000', 'Amd Ryzen 5000'), ('Intel_i5_12600', 'Intel I5 12600'), ('AMD_Ryzen_9_5900', 'Amd Ryzen 9 5900X'), ('Intel_i3_9100', 'Intel I3 9100')], max_length=70, null=True),
        ),
    ]
