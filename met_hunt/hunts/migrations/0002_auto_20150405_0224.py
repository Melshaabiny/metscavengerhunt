# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hunts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='has',
            old_name='hunts',
            new_name='hunt',
        ),
        migrations.RenameField(
            model_name='has',
            old_name='items',
            new_name='item',
        ),
    ]
