# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 02:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseDatos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BDNombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('BDDescripcion', models.CharField(blank=True, max_length=100, null=True, verbose_name='Descripci\xf3n')),
            ],
        ),
    ]
