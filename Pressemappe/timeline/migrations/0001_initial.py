# Generated by Django 3.0.5 on 2020-06-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pm20id', models.TextField()),
                ('wikidata_object', models.URLField()),
                ('name', models.TextField()),
                ('birthday', models.TextField()),
                ('deathday', models.TextField(null=True)),
                ('position_held', models.TextField()),
                ('position_held_startdate', models.TextField()),
                ('position_held_enddate', models.TextField()),
                ('picture', models.TextField(null=True)),
                ('gender', models.TextField(null=True)),
                ('religion', models.TextField(default='-')),
                ('predecessor', models.TextField(null=True)),
                ('successor', models.TextField(null=True)),
                ('country', models.TextField()),
            ],
        ),
    ]
