# Generated by Django 5.0.3 on 2024-03-19 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_request_requestimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='complaintBy',
            field=models.TextField(),
        ),
    ]