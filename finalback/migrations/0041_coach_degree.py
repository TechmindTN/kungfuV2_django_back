# Generated by Django 3.2.12 on 2022-12-13 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0040_auto_20221213_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='degree',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.degree'),
            preserve_default=False,
        ),
    ]