# Generated by Django 3.1.13 on 2021-07-27 07:33

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_profile_bio'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='profile',
            managers=[
                ('SearchEntry', django.db.models.manager.Manager()),
            ],
        ),
    ]
