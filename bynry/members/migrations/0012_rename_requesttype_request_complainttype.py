# Generated by Django 5.0.3 on 2024-03-19 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0011_rename_complainttype_request_requesttype'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='requestType',
            new_name='complaintType',
        ),
    ]