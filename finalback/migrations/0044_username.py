# Generated by Django 3.2.12 on 2022-12-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalback', '0043_auto_20221216_1512'),
    ]

    operations = [
        migrations.CreateModel(
            name='Username',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_username', models.TextField(default=1000000000, max_length=10, unique=True)),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]