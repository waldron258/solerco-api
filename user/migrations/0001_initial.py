# Generated by Django 5.0.4 on 2024-04-07 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('role', models.CharField(default='customer', max_length=100)),
                ('permissions', models.CharField(default='["read"]', max_length=100)),
                ('is_staff', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]