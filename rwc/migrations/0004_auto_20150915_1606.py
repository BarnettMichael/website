# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0003_auto_20150915_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='guess',
            name='team_chosen',
        ),
        migrations.RemoveField(
            model_name='match',
            name='away_team',
        ),
        migrations.RemoveField(
            model_name='match',
            name='home_team',
        ),
        migrations.AddField(
            model_name='match',
            name='points_difference',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='match',
            name='winning_team',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='points',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='match',
            name='team',
            field=models.ForeignKey(to='rwc.Team', null=True),
        ),
    ]
