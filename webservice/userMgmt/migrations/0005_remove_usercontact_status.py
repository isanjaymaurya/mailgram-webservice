# Generated by Django 4.2.7 on 2023-11-25 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userMgmt', '0004_usercontact_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercontact',
            name='status',
        ),
    ]
