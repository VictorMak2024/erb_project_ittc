# Generated by Django 4.2.19 on 2025-04-23 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salesmens', '0003_alter_salesmen_phone'),
        ('courses', '0003_remove_course_is_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='salesmen',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='salesmens.salesmen'),
        ),
    ]
