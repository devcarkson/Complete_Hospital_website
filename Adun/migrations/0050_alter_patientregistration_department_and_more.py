# Generated by Django 4.2.3 on 2023-09-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0049_alter_patientregistration_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientregistration',
            name='department',
            field=models.CharField(choices=[('Department of Biology and Forensic Science', 'Dbfs'), ('Department of Computing Science', 'Dcos'), ('Department of Public Law and Private Law', 'Dplp'), ('Department of Accounting/Business Administration/Economics', 'Dabae'), ('Department of English & Literary Studies/History & International Studies', 'Delhi'), ('Department of International Relations/Hospitality & Tourism Studies', 'Dit')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='faculty',
            field=models.CharField(choices=[('Faculty', 'fos'), ('Faculty of Science', 'fos'), ('Faculty of Arts and Management Science', 'fams'), ('Faculty of Law', 'fol')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='maritalstat',
            field=models.CharField(choices=[('gender', 'Gender'), ('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorced')], max_length=100, null=True),
        ),
    ]