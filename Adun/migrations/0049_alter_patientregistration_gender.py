# Generated by Django 4.2.3 on 2023-09-01 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0048_alter_patientregistration_room_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientregistration',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male')], max_length=6, null=True),
        ),
    ]
