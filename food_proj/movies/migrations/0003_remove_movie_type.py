# Generated by Django 5.0.3 on 2024-04-02 10:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_movie_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='type',
        ),
    ]
