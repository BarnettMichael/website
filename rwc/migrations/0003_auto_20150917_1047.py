# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0002_auto_20150916_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='match',
            field=models.ForeignKey(to='rwc.Match'),
        ),
        migrations.AlterField(
            model_name='guess',
            name='points_difference',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='guess',
            name='winning_team',
            field=models.ForeignKey(blank=True, to='rwc.Team', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(to='rwc.User'),
        ),
    ]
