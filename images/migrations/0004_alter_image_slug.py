# Generated by Django 4.1.3 on 2022-12-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0003_alter_image_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=500),
        ),
    ]
