# Generated by Django 4.1.4 on 2022-12-27 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='Ulasan',
            field=models.TextField(blank=True),
        ),
    ]