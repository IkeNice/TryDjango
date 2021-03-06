# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-03-16 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pydb', '0004_auto_20200316_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dancer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dancer_name', models.CharField(max_length=120, verbose_name='Имя танцора')),
                ('crew_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pydb.Crew')),
                ('style_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pydb.Style')),
            ],
        ),
    ]
