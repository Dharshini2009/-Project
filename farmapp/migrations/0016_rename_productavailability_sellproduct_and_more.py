# Generated by Django 4.2.5 on 2023-10-09 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farmapp', '0015_productavailability'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAvailability',
            new_name='Sellproduct',
        ),
        migrations.RenameField(
            model_name='sellproduct',
            old_name='name1',
            new_name='name',
        ),
    ]
