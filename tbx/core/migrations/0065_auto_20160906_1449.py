# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-06 13:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('torchbox', '0064_aboutpagerelatedlinkbutton'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='HomePageClients',
            new_name='HomePageClient',
        ),
        migrations.RenameModel(
            old_name='StandardPageClients',
            new_name='StandardPageClient',
        ),
        migrations.AlterModelOptions(
            name='servicespageservice',
            options={'ordering': ['sort_order']},
        ),
    ]
