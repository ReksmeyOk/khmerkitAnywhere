# Generated by Django 3.1.2 on 2020-10-11 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0008_auto_20201011_0826'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo_credit_thumbnail1',
            field=models.CharField(default='?', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_credit_thumbnail2',
            field=models.CharField(default='?', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_credit_thumbnail3',
            field=models.CharField(default='?', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_credit_thumbnailIndex',
            field=models.CharField(default='?', max_length=50),
        ),
    ]
