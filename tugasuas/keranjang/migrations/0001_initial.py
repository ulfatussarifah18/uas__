# Generated by Django 4.1.4 on 2022-12-27 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='keranjang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Toko', models.CharField(max_length=50)),
                ('Jumlah', models.CharField(max_length=10)),
                ('Variasi', models.CharField(max_length=10)),
                ('Pilihan', models.CharField(max_length=50)),
            ],
        ),
    ]
