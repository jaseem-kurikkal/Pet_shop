# Generated by Django 4.1.7 on 2023-03-08 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_sellapplication_user'),
        ('appointment', '0003_remove_bookappointment_booking_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookappointment',
            name='pet_name',
        ),
        migrations.AddField(
            model_name='bookappointment',
            name='category',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='product.category'),
            preserve_default=False,
        ),
    ]
