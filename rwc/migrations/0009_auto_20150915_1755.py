# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0008_auto_20150915_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='guess',
            name='match',
            field=models.ForeignKey(to='rwc.Match', null=True),
        ),
        migrations.AlterField(
            model_name='guess',
            name='team_chosen',
            field=models.ForeignKey(to='rwc.Team', null=True),
        ),
    ]
