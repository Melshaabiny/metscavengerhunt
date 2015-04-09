# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Has',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('clue', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hunts',
            fields=[
                ('Title', models.CharField(max_length=200)),
                ('ID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('ID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=200)),
                ('partof', models.ManyToManyField(to='hunts.Hunts', through='hunts.Has')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='has',
            name='hunts',
            field=models.ForeignKey(to='hunts.Hunts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has',
            name='items',
            field=models.ForeignKey(to='hunts.Items'),
            preserve_default=True,
        ),
    ]
