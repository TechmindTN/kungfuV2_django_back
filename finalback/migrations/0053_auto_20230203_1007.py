# Generated by Django 3.2.12 on 2023-02-03 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0052_result_notes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='p1_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='p2_points',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='winner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.athlete'),
        ),
    ]
