# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0004_has_hint'),
    ]

    operations = [
        migrations.AddField(
            model_name='has',
            name='image',
            field=models.CharField(default=b'No image available', max_length=250),
            preserve_default=True,
        ),
    ]
