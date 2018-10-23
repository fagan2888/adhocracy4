# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-19 11:57
from __future__ import unicode_literals

import adhocracy4.maps.fields
import adhocracy4.projects.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('a4administrative_districts', '0001_initial'),
        ('a4projects', '0017_contact_phone_regex'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='administrative_district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='a4administrative_districts.AdministrativeDistrict', verbose_name='Administrative district'),
        ),
        migrations.AddField(
            model_name='project',
            name='point',
            field=adhocracy4.maps.fields.PointField(blank=True, verbose_name='Location of your Project'),
        ),
        migrations.AddField(
            model_name='project',
            name='topic',
            field=adhocracy4.projects.fields.TopicField(blank=True, default='', max_length=254, verbose_name='Project topic'),
        ),
    ]
