# Generated by Django 5.0.4 on 2024-04-06 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0010_alter_carousel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
