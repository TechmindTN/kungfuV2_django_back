# Generated by Django 3.2.12 on 2023-02-16 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0057_alter_arbitrator_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='athlete',
            name='discipline',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.discipline'),
        ),
    ]