# Generated by Django 5.1.3 on 2024-11-21 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crm',
            old_name='tour',
            new_name='hotel',
        ),
    ]
