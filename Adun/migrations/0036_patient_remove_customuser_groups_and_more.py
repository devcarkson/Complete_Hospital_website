# Generated by Django 4.2.3 on 2023-08-27 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0035_remove_customuser_comfirm_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('admission_number', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('date_of_birth', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=10)),
                ('marital_status', models.CharField(max_length=10)),
                ('faculty', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('room_number', models.IntegerField()),
                ('weight', models.FloatField()),
                ('height', models.FloatField()),
                ('allergies', models.TextField()),
                ('medical_condition', models.TextField()),
                ('taking_medications', models.BooleanField()),
                ('medications', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='StaffRegistration',
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
