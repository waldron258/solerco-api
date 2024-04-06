# Generated by Django 5.0.4 on 2024-04-06 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carousel', '0005_alter_carousel_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/carousel'),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]