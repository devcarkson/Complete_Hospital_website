# Generated by Django 4.2.3 on 2023-08-12 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0017_rename_appointment_text_homecontent'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomeContent',
            new_name='ApointmentContent',
        ),
    ]