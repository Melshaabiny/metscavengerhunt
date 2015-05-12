# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0006_has_fact'),
    ]

    operations = [
        migrations.CreateModel(
            name='cr_Has',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('clue', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='cr_Hunts',
            fields=[
                ('ID', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('Title', models.CharField(max_length=200)),
                ('Category', models.CharField(max_length=200)),
                ('Start', models.CharField(max_length=400)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='cr_has',
            name='hunt',
            field=models.ForeignKey(to='cr_hunt.cr_Hunts'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cr_has',
            name='item',
            field=models.ForeignKey(to='hunts.Items'),
            preserve_default=True,
        ),
    ]
