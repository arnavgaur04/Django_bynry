# Generated by Django 5.0.3 on 2024-03-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0004_alter_request_complaintby'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='complaintType',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='complaintBy',
            field=models.IntegerField(null=True),
        ),
    ]
