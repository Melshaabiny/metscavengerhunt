# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0006_auto_20150406_2001'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='description',
            field=models.CharField(max_length=500, blank=True),
            preserve_default=True,
        ),
    ]
