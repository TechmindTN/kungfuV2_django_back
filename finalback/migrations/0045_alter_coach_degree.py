# Generated by Django 3.2.12 on 2022-12-22 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0044_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coach',
            name='degree',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.degree'),
        ),
    ]
