# Generated by Django 4.0.5 on 2022-06-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ambulanceapp', '0009_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='town',
            field=models.CharField(max_length=20),
        ),
    ]
