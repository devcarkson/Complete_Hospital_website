# Generated by Django 4.2.3 on 2023-08-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0032_rename_password1_staffregistration_comfirm_password_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patientregistration',
            old_name='password1',
            new_name='comfirm_password',
        ),
        migrations.RenameField(
            model_name='patientregistration',
            old_name='password2',
            new_name='password',
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='faculty',
            field=models.CharField(choices=[('fos', 'Faculty'), ('fos', 'Faculty of Science'), ('fams', 'Faculty of Arts and Management Science'), ('fol', 'Faculty of Law')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='patientregistration',
            name='maritalstat',
            field=models.CharField(choices=[('gender', 'Gender'), ('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorced')], max_length=10, null=True),
        ),
    ]
