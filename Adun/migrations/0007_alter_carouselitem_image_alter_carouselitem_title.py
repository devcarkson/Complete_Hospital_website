# Generated by Django 4.2.3 on 2023-08-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adun', '0006_carouselitem_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carouselitem',
            name='image',
            field=models.ImageField(upload_to='carousel/%y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='carouselitem',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
