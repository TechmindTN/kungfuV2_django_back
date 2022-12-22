# Generated by Django 3.2.12 on 2022-12-22 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0046_auto_20221222_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arbitrator',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.club'),
        ),
        migrations.AlterField(
            model_name='athlete',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.club'),
        ),
        migrations.AlterField(
            model_name='coach',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.club'),
        ),
        migrations.AlterField(
            model_name='supporter',
            name='club',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='finalback.club'),
        ),
    ]
