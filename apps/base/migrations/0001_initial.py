# Generated by Django 4.0 on 2022-05-20 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSliders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slider_text', models.CharField(max_length=101)),
            ],
            options={
                'verbose_name': 'Home Slider',
                'verbose_name_plural': 'Home Sliders',
            },
        ),
    ]
