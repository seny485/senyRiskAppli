# Generated by Django 2.1.15 on 2020-07-23 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='declaration',
            name='circuit',
        ),
    ]
