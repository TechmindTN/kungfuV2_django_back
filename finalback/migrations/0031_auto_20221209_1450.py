# Generated by Django 3.2.12 on 2022-12-09 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0030_competition_attendents'),
    ]

    operations = [
        migrations.AddField(
            model_name='athlete',
            name='medical_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/athlete/medical'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='idantity_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/athlete/identity'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/athlete/photo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='image/profile/'),
        ),
    ]
