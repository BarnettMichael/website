# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('carbs', models.IntegerField()),
                ('sugar', models.IntegerField()),
                ('protein', models.IntegerField()),
                ('fat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.UUIDField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('calories', models.PositiveIntegerField()),
            ],
        ),
    ]
