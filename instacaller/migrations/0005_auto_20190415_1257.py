# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-15 07:27
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instacaller', '0004_auto_20190415_1240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdb',
            name='phone',
        ),
        migrations.AddField(
            model_name='userdb',
            name='phone_number',
            field=models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]