# Generated by Django 5.1.4 on 2024-12-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMS', '0007_merge_0004_profile_image_0006_alter_attendance_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aadhar_card',
            field=models.FileField(blank=True, null=True, upload_to='aadhar_cards/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv_files/'),
        ),
    ]
