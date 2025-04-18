# Generated by Django 4.2.20 on 2025-04-05 18:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('soundBody', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='musician',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='musician',
            name='joinDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='trainer',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='trainer',
            name='joinDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
