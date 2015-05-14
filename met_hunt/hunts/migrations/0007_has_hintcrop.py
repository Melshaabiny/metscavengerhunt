# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0006_has_fact'),
    ]

    operations = [
        migrations.AddField(
            model_name='has',
            name='hintcrop',
            field=models.CharField(default=b'No hintcrop available', max_length=200),
            preserve_default=True,
        ),
    ]
