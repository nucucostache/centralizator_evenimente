# Generated by Django 4.2.23 on 2025-07-02 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.CharField(choices=[('curs', 'Curs'), ('workshop', 'Workshop')], default='curs', max_length=20),
        ),
    ]
