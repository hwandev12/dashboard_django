# Generated by Django 4.0 on 2022-05-23 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('base', '0005_phoneaccessories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(default='redmi.jpg', upload_to='')),
                ('bio', models.TextField()),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='authentication.user')),
            ],
        ),
    ]