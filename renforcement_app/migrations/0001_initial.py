# Generated by Django 3.2.5 on 2021-07-30 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course_name', models.CharField(max_length=100)),
                ('Year', models.CharField(max_length=20)),
                ('Link', models.CharField(max_length=2000)),
            ],
        ),
    ]
