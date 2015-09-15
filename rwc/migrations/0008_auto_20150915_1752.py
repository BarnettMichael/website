# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0007_auto_20150915_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guess',
            name='match',
        ),
        migrations.AddField(
            model_name='guess',
            name='team_chosen',
            field=models.ForeignKey(default=None, to='rwc.Team'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.ForeignKey(blank=True, to='rwc.Team', null=True),
        ),
    ]
