# Generated by Django 4.0 on 2022-05-25 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_remove_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
