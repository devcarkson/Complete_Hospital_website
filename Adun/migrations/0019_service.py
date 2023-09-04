# Generated by Django 4.2.3 on 2023-08-12 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0018_rename_homecontent_apointmentcontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
    ]
