# Generated by Django 4.2.7 on 2023-11-25 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaignMgmt', '0004_rename_campaing_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='dynamic_values',
            field=models.JSONField(default={}),
        ),
    ]
