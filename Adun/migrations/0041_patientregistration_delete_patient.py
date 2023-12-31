# Generated by Django 4.2.3 on 2023-08-29 09:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0040_patient_delete_patientregistration'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientRegistration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=30, null=True, unique=True)),
                ('comfirm_password', models.CharField(max_length=30, null=True, unique=True)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('gender', models.CharField(choices=[('girl', 'Female'), ('boy', 'Male')], max_length=4, null=True)),
                ('maritalstat', models.CharField(choices=[('gender', 'Gender'), ('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorced')], max_length=10, null=True)),
                ('faculty', models.CharField(choices=[('fos', 'Faculty'), ('fos', 'Faculty of Science'), ('fams', 'Faculty of Arts and Management Science'), ('fol', 'Faculty of Law')], max_length=10, null=True)),
                ('department', models.CharField(choices=[('Dbfs', 'Department of Biology and Forensic Science'), ('Dcos', 'Department of Computing Science'), ('Dplp', 'Department of Public Law and Private Law'), ('Dabae', 'Department of Accounting/Business Administration/Economics'), ('Delhi', 'Department of English & Literary Studies/History & International Studies'), ('Dit', 'Department of International Relations/Hospitality & Tourism Studies')], max_length=10, null=True)),
                ('admission_number', models.CharField(max_length=20, null=True)),
                ('room_number', models.PositiveIntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(75)])),
                ('weight', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('height', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('allergies', models.TextField(null=True)),
                ('medical_condition', models.TextField(null=True)),
                ('taking_medications', models.BooleanField(null=True)),
                ('medications', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]
