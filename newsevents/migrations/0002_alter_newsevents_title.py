# Generated by Django 4.2.19 on 2025-04-18 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsevents', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsevents',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
