# Generated by Django 4.2.19 on 2025-04-22 02:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('supportresources', '0009_delete_supportresource'),
        ('srdetails', '0007_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Srdetail',
        ),
    ]
