# Generated by Django 3.2.15 on 2022-08-19 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_alter_place_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(max_length=200)),
                ('image', models.ImageField(upload_to='photo')),
                ('title', models.CharField(max_length=100)),
                ('subhead', models.TextField(max_length=20)),
                ('desc', models.TextField()),
            ],
        ),
    ]