# Generated by Django 4.1.1 on 2022-10-03 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0015_profile_birthday_profile_cin_profile_first_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='categorie_age',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
