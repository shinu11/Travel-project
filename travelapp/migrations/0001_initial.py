# Generated by Django 3.2.15 on 2022-08-17 08:09
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('desc', models.TextField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default='false')),
            ],
        ),
    ]
