# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rwc', '0004_auto_20150917_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='winning_team',
            field=models.ForeignKey(blank=True, to='rwc.Team', null=True),
        ),
    ]
