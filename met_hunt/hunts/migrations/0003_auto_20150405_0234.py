# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0002_auto_20150405_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='ID',
            field=models.CharField(max_length=20, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
