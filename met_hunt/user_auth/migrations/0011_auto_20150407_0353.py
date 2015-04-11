# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0010_auto_20150407_0346'),
    ]

    operations = [
        migrations.AddField(
            model_name='answered',
            name='when',
            field=models.DateField(default=datetime.datetime(2015, 4, 7, 3, 53, 5, 432946, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='questionasked',
            name='when',
            field=models.DateField(default=datetime.datetime(2015, 4, 7, 3, 53, 17, 403657, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
