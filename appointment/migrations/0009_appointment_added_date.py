# Generated by Django 4.1.7 on 2023-03-18 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0008_bookappointment_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='added_date',
            field=models.DateField(auto_now_add=True, default='2023-03-18'),
            preserve_default=False,
        ),
    ]
