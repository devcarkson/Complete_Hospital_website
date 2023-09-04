# Generated by Django 4.2.3 on 2023-08-21 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0026_remove_patientregistration_admission_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientregistration',
            name='admission_number',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='allergies',
            field=models.TextField(default='ekemem'),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='department',
            field=models.CharField(choices=[('Dbfs', 'Department of Biology and Forensic Science'), ('Dcos', 'Department of Computing Science'), ('Dplp', 'Department of Public Law and Private Law'), ('Dabae', 'Department of Accounting/Business Administration/Economics'), ('Delhi', 'Department of English & Literary Studies/History & International Studies'), ('Dit', 'Department of International Relations/Hospitality & Tourism Studies')], default='Dbfs', max_length=10),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='faculty',
            field=models.CharField(choices=[('fos', 'Faculty of Science'), ('fams', 'Faculty of Arts and Management Science'), ('fol', 'Faculty of Law')], default='Dbfs', max_length=10),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='gender',
            field=models.CharField(choices=[('girl', 'Female'), ('boy', 'Male')], default='Male', max_length=4),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='maritalstat',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorced')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='medical_condition',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='medications',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='room_number',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(75)]),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='taking_medications',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='patientregistration',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='first_name',
            field=models.CharField(default='ekemem', max_length=50),
        ),
    ]
