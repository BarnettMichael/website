# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calorie_calculator', '0002_auto_20160905_1307'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instruction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instruction', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(to='calorie_calculator.Ingredient'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='macros',
            field=models.CommaSeparatedIntegerField(max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbs',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='fat',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sugar',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='id',
            field=models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True),
        ),
        migrations.AddField(
            model_name='instruction',
            name='recipe',
            field=models.ForeignKey(to='calorie_calculator.Recipe'),
        ),
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=models.ManyToManyField(to='calorie_calculator.Tag'),
        ),
    ]
