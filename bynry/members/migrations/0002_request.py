# Generated by Django 5.0.3 on 2024-03-19 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaintBy', models.IntegerField()),
                ('requestDetails', models.TextField()),
                ('requestDate', models.DateField(default=datetime.date(2024, 3, 19))),
                ('requestImage', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
