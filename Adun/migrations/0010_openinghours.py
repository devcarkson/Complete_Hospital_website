# Generated by Django 4.2.3 on 2023-08-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0009_bannercontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=20)),
                ('hours', models.CharField(max_length=50)),
            ],
        ),
    ]
