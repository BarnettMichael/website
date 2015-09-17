# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0003_auto_20150917_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.ForeignKey(choices=[(models.ForeignKey(related_name='home_team', to='rwc.Team', null=True), None), (models.ForeignKey(related_name='away_team', to='rwc.Team', null=True), None)], to='rwc.Team', blank=True, null=True),
        ),
    ]
