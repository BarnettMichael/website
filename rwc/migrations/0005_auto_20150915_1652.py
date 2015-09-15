# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0004_auto_20150915_1606'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='match',
            name='team',
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(related_name='away_team', to='rwc.Team', null=True),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(related_name='home_team', to='rwc.Team', null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.CharField(blank=True, max_length=200, choices=[(b'home_team.Team', b'home team'), (b'away_team.Team', b'away_team')]),
        ),
        migrations.AlterField(
            model_name='team',
            name='name',
            field=models.CharField(max_length=200, unique=True, null=True),
        ),
    ]
