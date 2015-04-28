# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0008_auto_20150407_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionasked',
            name='status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
