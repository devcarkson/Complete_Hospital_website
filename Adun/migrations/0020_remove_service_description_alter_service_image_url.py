# Generated by Django 4.2.3 on 2023-08-12 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0019_service'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='description',
        ),
        migrations.AlterField(
            model_name='service',
            name='image_url',
            field=models.ImageField(upload_to='AboutUs/%y/%m/%d/'),
        ),
    ]