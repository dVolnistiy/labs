# Generated by Django 4.0 on 2021-12-16 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0014_remove_proc_id_proc_remove_proc_processor_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Proc',
        ),
        migrations.AddField(
            model_name='pc',
            name='hdd',
            field=models.CharField(choices=[('SSD_ExeGate_Next_60GB', 'Ssd Exegate Next 60Gb'), ('Seagate_Video_3_320GB', 'Seagate Video 3 320Gb'), ('SSD_AMD_Radeon_R5_128GB', 'Ssd Amd Radeon R5 128Gb'), ('WESTERN_DIGITAL_AV_GP_500GB', 'Western Digital Av Gp 500Gb')], help_text='Choose hdd for PC', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pc',
            name='memmory',
            field=models.CharField(choices=[('16GB_DDR4_2666', 'Ram 16Gb Ddr4 2666'), ('8GB_DDR4_2666', 'Ram 8Gb Ddr4 2666'), ('4GB_DDR3L_1866', 'Ram 4Gb Ddr3L 1866'), ('2GB_DDR3L_1600', 'Ram 2Gb Ddr3L 1600')], help_text='Choose memmory for PC', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='processor',
            field=models.CharField(choices=[('AMD_Ryzen_5000', 'Amd Ryzen 5000'), ('Intel_i5_12600', 'Intel I5 12600'), ('AMD_Ryzen_9_5900', 'Amd Ryzen 9 5900X'), ('Intel_i3_9100', 'Intel I3 9100')], help_text='Choose processor for PC', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='time_of_setup',
            field=models.DateField(help_text='When computer delivered to the room', null=True),
        ),
        migrations.AlterField(
            model_name='pc',
            name='videocard',
            field=models.CharField(choices=[('ASUS_Geforce_GTX_1050_Ti', 'Asus Geforce Gtx 1050 Ti'), ('HP_Radeon_HD_7670', 'Hp Radeon Hd 7670'), ('AMD_Radeon_HD8490', 'Amd Radeon Hd8490'), ('ASUS_GeForce_GT_710', 'Asus Geforce Gt 710')], help_text='Choose graphic card for PC', max_length=50, null=True),
        ),
    ]