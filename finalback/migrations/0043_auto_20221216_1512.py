# Generated by Django 3.2.12 on 2022-12-16 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0042_remove_coach_cin'),
    ]

    operations = [
        migrations.AddField(
            model_name='categorie',
            name='max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='categorie',
            name='min',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weights',
            name='max',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='weights',
            name='min',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
