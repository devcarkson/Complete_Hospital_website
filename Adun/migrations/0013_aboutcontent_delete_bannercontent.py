# Generated by Django 4.2.3 on 2023-08-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0012_appoint_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitle', models.CharField(max_length=200)),
                ('intro_text', models.TextField()),
                ('points', models.TextField()),
                ('image_url', models.URLField()),
            ],
        ),
        migrations.DeleteModel(
            name='BannerContent',
        ),
    ]
