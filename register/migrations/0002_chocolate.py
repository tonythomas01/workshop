# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chocolate',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='Chocolate Name', blank=True)),
                ('description', models.CharField(max_length=1000, verbose_name='Chocolate Description', blank=True)),
                ('manufacturer', models.CharField(max_length=100, verbose_name='Chocolate Manufacturer', blank=True)),
                ('price', models.IntegerField(blank=True, help_text='4 digits maximum', null=True, verbose_name='Chocolate Price', validators=[django.core.validators.MaxValueValidator(1000), django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]
