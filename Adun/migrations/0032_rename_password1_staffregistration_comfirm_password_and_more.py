# Generated by Django 4.2.3 on 2023-08-23 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0031_remove_staffregistration_admission_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffregistration',
            old_name='password1',
            new_name='comfirm_password',
        ),
        migrations.RenameField(
            model_name='staffregistration',
            old_name='password2',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='staffregistration',
            old_name='department',
            new_name='qualification',
        ),
    ]
