# Generated by Django 3.2.12 on 2022-12-13 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0037_auto_20221213_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.TextField(),
        ),
    ]
