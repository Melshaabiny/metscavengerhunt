# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0003_auto_20150408_0243'),
    ]

    operations = [
        migrations.AddField(
            model_name='has',
            name='hint',
            field=models.CharField(default=b'No hint available', max_length=200),
            preserve_default=True,
        ),
    ]
