# Generated by Django 4.2.3 on 2023-08-25 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_alter_user_first_name_alter_user_last_name'),
        ('Adun', '0034_customuser_delete_patientregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='comfirm_password',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='department',
            field=models.CharField(choices=[('Dbfs', 'Department of Biology and Forensic Science'), ('Dcos', 'Department of Computing Science'), ('Dplp', 'Department of Public Law and Private Law'), ('Dabae', 'Department of Accounting/Business Administration/Economics'), ('Delhi', 'Department of English & Literary Studies/History & International Studies'), ('Dit', 'Department of International Relations/Hospitality & Tourism Studies')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='faculty',
            field=models.CharField(choices=[('fos', 'Faculty of Science'), ('fams', 'Faculty of Arts and Management Science'), ('fol', 'Faculty of Law')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='first name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_set_for_groups_%(app_label)s_%(class)s_last_name', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='last name'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='maritalstat',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorce', 'Divorced')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default=3, max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='customuser_set_for_user_permissions_%(app_label)s_%(class)s_last_name', to='auth.permission', verbose_name='user permissions'),
        ),
    ]
