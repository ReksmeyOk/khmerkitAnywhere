# Generated by Django 3.1.2 on 2020-10-09 03:31

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mathapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math_unit',
            name='article1',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='math_unit',
            name='article2',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='math_unit',
            name='article3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='math_unit',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
