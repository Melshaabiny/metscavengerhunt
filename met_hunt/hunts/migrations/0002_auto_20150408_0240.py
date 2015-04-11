# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='has',
            name='number',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
