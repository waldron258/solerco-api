# Generated by Django 5.0.4 on 2024-04-07 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kit',
            name='images_url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='images_url',
        ),
    ]