# Generated by Django 4.2.3 on 2023-08-20 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0023_student_reg'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='student_reg',
            new_name='patient_reg',
        ),
    ]