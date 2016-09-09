# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_calculator', '0003_auto_20160909_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='ingredients_dictionary',
            field=jsonfield.fields.JSONField(null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='macros',
            field=models.CommaSeparatedIntegerField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='calorie_calculator.Tag', null=True),
        ),
    ]
