# Generated by Django 2.2.6 on 2019-11-01 14:56

import adhocracy4.projects.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a4projects', '0025_change_helptext_is_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_type',
            field=adhocracy4.projects.fields.TypeField(blank=True, default='', max_length=254),
        ),
    ]
