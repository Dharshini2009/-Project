# Generated by Django 4.2.5 on 2023-10-08 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0013_productavailability'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProductAvailability',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
