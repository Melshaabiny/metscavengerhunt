# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0002_auto_20150408_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hunts',
            name='Start',
            field=models.CharField(max_length=400),
            preserve_default=True,
        ),
    ]
