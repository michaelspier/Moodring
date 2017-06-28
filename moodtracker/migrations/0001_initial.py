# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rec_date', models.DateTimeField(verbose_name='date recorded')),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_value', models.SmallIntegerField()),
                ('y_value', models.SmallIntegerField()),
                ('description', models.TextField()),
                ('rec_date', models.DateTimeField(verbose_name='date recorded')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moodtracker.Event_Type'),
        ),
    ]
