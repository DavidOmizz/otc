# Generated by Django 4.2.15 on 2024-08-13 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CohortInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=200)),
                ('niche', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('student', models.CharField(max_length=20)),
            ],
        ),
    ]
