# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 14:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0028_auto_20171122_1448'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='NewSentFullReport',
            new_name='SentFullReport',
        ),
    ]