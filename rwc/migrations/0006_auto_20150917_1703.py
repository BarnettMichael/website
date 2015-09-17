# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0005_auto_20150917_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guess',
            old_name='points_difference',
            new_name='score_difference',
        ),
        migrations.RenameField(
            model_name='match',
            old_name='points_difference',
            new_name='score_difference',
        ),
    ]
