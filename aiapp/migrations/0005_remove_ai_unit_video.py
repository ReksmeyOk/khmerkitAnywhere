# Generated by Django 3.1.2 on 2021-01-27 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aiapp', '0004_auto_20201011_0809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ai_unit',
            name='video',
        ),
    ]
