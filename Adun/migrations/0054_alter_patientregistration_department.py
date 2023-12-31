# Generated by Django 4.2.3 on 2023-09-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0053_alter_patientregistration_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientregistration',
            name='department',
            field=models.CharField(choices=[('Select', 'Select'), ('Department of Biology and Forensic Science', 'Department of Biology and Forensic Science'), ('Department of Computing Science', 'Department of Computing Science'), ('Department of Public Law and Private Law', 'Department of Public Law and Private Law'), ('Department of Accounting/Business Administration/Economics', 'Department of Accounting/Business Administration/Economics'), ('Department of English & Literary Studies/History & International Studies', 'Department of English & Literary Studies/History & International Studies'), ('Department of International Relations/Hospitality & Tourism Studies', 'Department of International Relations/Hospitality & Tourism Studies')], max_length=100, null=True),
        ),
    ]
