# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 20:49
from __future__ import unicode_literals

from django.db import migrations, models


def copy_site_to_sites(apps, schema_editor):
    current_database = schema_editor.connection.alias
    PageBase = apps.get_model('wizard_builder.PageBase')
    for page in PageBase.objects.using(current_database).filter(site__isnull=False):
        page.sites.add(page.site.id)

def copy_sites_to_site(apps, schema_editor):
    current_database = schema_editor.connection.alias
    PageBase = apps.get_model('wizard_builder.PageBase')
    for page in PageBase.objects.using(current_database):
        site_id = page.sites.first().id
        PageBase.objects.using(current_database).update(site=site_id)

class Migration(migrations.Migration):

    dependencies = [
        ('wizard_builder', '0005_delete_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagebase',
            name='sites',
            field=models.ManyToManyField(to='sites.Site', null=True),
        ),
        migrations.RunPython(
            copy_site_to_sites,
            reverse_code=copy_sites_to_site,
        ),
        migrations.RemoveField(
            model_name='pagebase',
            name='site',
        ),
    ]
