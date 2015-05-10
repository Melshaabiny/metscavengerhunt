# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0005_has_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='has',
            name='fact',
            field=models.CharField(default=b'No fact available', max_length=250),
            preserve_default=True,
        ),
    ]
