# Generated by Django 4.2 on 2023-04-08 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeviceManagementApp', '0002_rename_id_deviceinstance_deviceid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deviceinstance',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
