# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0009_auto_20150407_0341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answered',
            name='answeredBy',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
