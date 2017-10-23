# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cluster', '0001_initial'),
        ('core', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='imo_clusters',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='cluster.Cluster'),
        ),
        migrations.AddField(
            model_name='user',
            name='workspaces',
            field=models.ManyToManyField(blank=True, null=True, related_name='users', to='core.Workspace'),
        ),
    ]
