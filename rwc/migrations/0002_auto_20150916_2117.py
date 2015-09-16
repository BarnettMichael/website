# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guess',
            old_name='score_chosen',
            new_name='points_difference',
        ),
        migrations.RenameField(
            model_name='guess',
            old_name='team_chosen',
            new_name='winning_team',
        ),
    ]
