# Generated by Django 3.0.5 on 2020-04-25 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('levels', '0004_auto_20200425_1911'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pollution_index',
            name='area',
        ),
    ]
