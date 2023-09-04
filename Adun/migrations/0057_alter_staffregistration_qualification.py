# Generated by Django 4.2.3 on 2023-09-02 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0056_staffregistration_is_active_staffregistration_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffregistration',
            name='qualification',
            field=models.CharField(choices=[('Select', 'Select'), ('Doctor', 'Doctor'), ('Nurse', 'Nurse'), ('Pharmacist', 'Pharmacist'), ('Consultant', 'Consultant'), ('Laboratory', 'Laboratory')], max_length=30, null=True),
        ),
    ]