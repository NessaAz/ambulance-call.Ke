# Generated by Django 4.0.5 on 2022-06-24 02:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ambulanceapp', '0006_account_image_ambulanceprovider_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='uuid',
        ),
    ]
