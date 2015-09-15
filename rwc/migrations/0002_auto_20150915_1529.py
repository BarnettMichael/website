# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guess',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_chosen', models.CharField(max_length=200)),
                ('score_chosen', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.DateTimeField()),
                ('home_team', models.CharField(max_length=200)),
                ('away_team', models.CharField(max_length=200)),
                ('winning_team', models.CharField(max_length=200, null=True, choices=[(models.CharField(max_length=200), b'Home Team'), (models.CharField(max_length=200), b'Away Team')])),
                ('points_difference', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('points', models.PositiveSmallIntegerField(default=0, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='guess',
            name='author',
            field=models.ForeignKey(to='rwc.Person'),
        ),
        migrations.AddField(
            model_name='guess',
            name='match',
            field=models.ForeignKey(to='rwc.Match'),
        ),
    ]
