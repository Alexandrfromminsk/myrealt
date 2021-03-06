# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 21:50
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Criteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('description', models.TextField()),
                ('weight', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pseudonim', models.CharField(max_length=60)),
                ('link', models.TextField()),
                ('rating', models.FloatField()),
                ('is_ready', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='pseudonim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assess.Rating'),
        ),
        migrations.AddField(
            model_name='marks',
            name='weight',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assess.Criteria'),
        ),
    ]
