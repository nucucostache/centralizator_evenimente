# Generated by Django 5.2.3 on 2025-07-01 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_website_url'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
