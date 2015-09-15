# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0002_auto_20150915_1529'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guess',
            old_name='author',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='match',
            name='points_difference',
        ),
        migrations.RemoveField(
            model_name='match',
            name='winning_team',
        ),
    ]
