# Generated by Django 3.0.5 on 2020-04-25 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0003_pollution_index_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollution_index',
            name='date',
            field=models.DateField(),
        ),
    ]
