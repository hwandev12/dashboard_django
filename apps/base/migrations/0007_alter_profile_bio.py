# Generated by Django 4.0 on 2022-05-25 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True),
        ),
    ]