# Generated by Django 3.2.12 on 2023-03-02 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0058_alter_athlete_discipline'),
    ]

    operations = [
        migrations.AddField(
            model_name='coach',
            name='discipline',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.discipline'),
        ),
    ]