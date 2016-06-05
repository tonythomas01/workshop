# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('user_id', models.AutoField(serialize=False, primary_key=True)),
                ('user_first_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='First Name', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('user_last_name', models.CharField(blank=True, max_length=32, null=True, verbose_name='Last Name', validators=[django.core.validators.RegexValidator(regex=b'^[A-Za-z]*$')])),
                ('email', models.EmailField(unique=True, max_length=254, verbose_name='Email', db_index=True)),
                ('user_dob', models.DateField(null=True, verbose_name='Birth Date', blank=True)),
                ('user_gender', models.CharField(blank=True, max_length=1, null=True, verbose_name='Gender', choices=[(b'M', 'Male'), (b'F', 'Female')])),
                ('user_github', models.CharField(max_length=100, verbose_name='Github Profile', blank=True)),
                ('user_linkedin', models.CharField(max_length=100, verbose_name='Linkedin Profile', blank=True)),
                ('user_bio', models.CharField(max_length=1000, verbose_name='Short Bio', blank=True)),
                ('user_occupation', models.CharField(max_length=100, verbose_name='Occupation', blank=True)),
                ('user_nationality', models.CharField(max_length=100, verbose_name='Nationality', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(unique=True, max_length=32, verbose_name='username')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
