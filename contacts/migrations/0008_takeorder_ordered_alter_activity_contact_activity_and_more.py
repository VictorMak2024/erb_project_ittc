# Generated by Django 4.2.19 on 2025-04-22 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_remove_course_is_paid'),
        ('activities', '0003_remove_activity_is_paid'),
        ('products', '0002_alter_product_title'),
        ('contacts', '0007_takeorder_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='takeorder',
            name='ordered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='activity_contact',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='activities.activity'),
        ),
        migrations.AlterField(
            model_name='course_contact',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='courses.course'),
        ),
        migrations.AlterField(
            model_name='product_contact',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
        migrations.AlterField(
            model_name='takeorder',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.product'),
        ),
    ]
