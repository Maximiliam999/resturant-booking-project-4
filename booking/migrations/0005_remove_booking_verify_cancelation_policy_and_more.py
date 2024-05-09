# Generated by Django 4.2.11 on 2024-05-09 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_remove_cancelbooking_id_cancelbooking_booking'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='verify_cancelation_policy',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='verify_length',
        ),
        migrations.AddField(
            model_name='booking',
            name='verify_cancellation_policy',
            field=models.BooleanField(default=False, help_text='Please check this box to confirm you have read and agree to the cancellation policy', verbose_name='Cancellation Policy Agreement'),
        ),
    ]
