# Generated by Django 3.1.12 on 2021-06-25 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='Hi I have not filled my Bio Yet'),
        ),
    ]