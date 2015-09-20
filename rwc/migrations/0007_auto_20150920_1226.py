# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0006_auto_20150917_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guess',
            name='score_difference',
            field=models.PositiveSmallIntegerField(default=0, null=True, blank=True),
        ),
    ]
