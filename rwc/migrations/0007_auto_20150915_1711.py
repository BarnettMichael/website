# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0006_auto_20150915_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.ForeignKey(choices=[(b'home_team.Team', b'home team'), (b'away_team.Team', b'away_team')], to='rwc.Team', blank=True, null=True),
        ),
    ]
