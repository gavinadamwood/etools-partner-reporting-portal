# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-12 06:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cluster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('type', models.CharField(choices=[('cccm', 'CCCM'), ('early_recovery', 'Early Recovery'), ('education', 'Education'), ('emergency_telecommunications', 'Emergency Telecommunications'), ('food_security', 'Food Security'), ('health', 'Health'), ('logistics', 'Logistics'), ('nutrition', 'Nutrition'), ('protection', 'Protection'), ('shelter', 'Shelter'), ('wash', 'WASH')], max_length=32)),
                ('response_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clusters', to='core.ResponsePlan')),
            ],
        ),
        migrations.CreateModel(
            name='ClusterActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255)),
                ('standard', models.CharField(max_length=255)),
                ('frequency', models.CharField(choices=[('Wee', 'Weekly'), ('Mon', 'Monthly'), ('Qua', 'Quarterly')], default='Mon', max_length=3, verbose_name='Frequency of reporting')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ClusterObjective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=255, verbose_name='Cluster Objective Title')),
                ('reference_number', models.CharField(max_length=255, verbose_name='Reference Number')),
                ('frequency', models.CharField(choices=[('Wee', 'Weekly'), ('Mon', 'Monthly'), ('Qua', 'Quarterly')], default='Mon', max_length=3, verbose_name='Frequency of reporting')),
                ('cluster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_objectives', to='cluster.Cluster')),
                ('locations', models.ManyToManyField(related_name='cluster_objectives', to='core.Location')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='clusteractivity',
            name='cluster_objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cluster_activities', to='cluster.ClusterObjective'),
        ),
        migrations.AddField(
            model_name='clusteractivity',
            name='locations',
            field=models.ManyToManyField(related_name='cluster_activities', to='core.Location'),
        ),
        migrations.AlterUniqueTogether(
            name='cluster',
            unique_together=set([('type', 'response_plan')]),
        ),
    ]
