# Generated by Django 4.1.7 on 2023-03-08 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0004_remove_bookappointment_pet_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookappointment',
            name='doc_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='appointment.appointment'),
            preserve_default=False,
        ),
    ]
