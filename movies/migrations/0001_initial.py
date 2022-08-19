# Generated by Django 4.1 on 2022-08-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('film_adı', models.CharField(max_length=200)),
                ('aciklama', models.TextField()),
                ('resim', models.CharField(max_length=100)),
                ('anasayfa', models.BooleanField(default=False)),
            ],
        ),
    ]
