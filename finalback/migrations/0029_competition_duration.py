# Generated by Django 3.2.12 on 2022-12-01 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0028_auto_20221201_1114'),
    ]

    operations = [
        migrations.AddField(
            model_name='competition',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
