# Generated by Django 4.2.5 on 2023-10-08 16:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('farmapp', '0008_rename_productavailability_productavailability1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductAvailability1',
            new_name='ProductAvailability',
        ),
        migrations.RenameModel(
            old_name='UserProfile1',
            new_name='UserProfile',
        ),
    ]