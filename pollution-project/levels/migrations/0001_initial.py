# Generated by Django 3.0.5 on 2020-04-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pollution_index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('pm25', models.IntegerField()),
                ('pm10', models.IntegerField()),
                ('o3', models.IntegerField()),
                ('no2', models.IntegerField()),
                ('so2', models.IntegerField()),
                ('co', models.IntegerField()),
            ],
        ),
    ]
