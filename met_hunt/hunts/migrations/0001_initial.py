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
                ('number', models.IntegerField(max_length=200)),
                ('clue', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hunts',
            fields=[
                ('ID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Start', models.CharField(default=b'Blank starting point', max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('ID', models.CharField(max_length=20, unique=True, serialize=False, primary_key=True)),
                ('Category', models.CharField(max_length=200)),
                ('partof', models.ManyToManyField(to='hunts.Hunts', through='hunts.Has')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='has',
            name='hunt',
            field=models.ForeignKey(to='hunts.Hunts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='has',
            name='item',
            field=models.ForeignKey(to='hunts.Items'),
            preserve_default=True,
        ),
    ]
