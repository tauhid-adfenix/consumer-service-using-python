# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 11:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='consumerservicemessages',
            table='consumer_service_messages',
        ),
    ]
