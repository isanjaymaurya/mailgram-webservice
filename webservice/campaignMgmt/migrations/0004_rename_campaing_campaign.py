# Generated by Django 4.2.7 on 2023-11-25 14:06

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userMgmt', '0005_remove_usercontact_status'),
        ('newsletterMgmt', '0002_newslettertemplate_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('campaignMgmt', '0003_campaing_status'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Campaing',
            new_name='Campaign',
        ),
    ]
