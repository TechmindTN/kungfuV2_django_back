# Generated by Django 3.2.12 on 2022-12-12 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0033_auto_20221212_1527'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='image/club'),
        ),
    ]
