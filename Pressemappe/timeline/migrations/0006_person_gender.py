# Generated by Django 3.0.5 on 2020-06-11 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0005_auto_20200611_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.TextField(null=True),
        ),
    ]
