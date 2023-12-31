# Generated by Django 4.2.3 on 2023-08-08 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0003_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='post_images/')),
            ],
        ),
    ]
