# Generated by Django 4.2.3 on 2023-08-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0014_remove_aboutcontent_points_aboutcontent_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutcontent',
            name='image_url',
            field=models.ImageField(upload_to='AboutUs/%y/%m/%d/'),
        ),
    ]