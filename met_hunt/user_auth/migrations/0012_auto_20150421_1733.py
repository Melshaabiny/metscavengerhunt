# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0011_auto_20150407_0353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answered',
            name='answeredBy',
        ),
        migrations.RemoveField(
            model_name='answered',
            name='questionBy',
        ),
        migrations.DeleteModel(
            name='Answered',
        ),
        migrations.RemoveField(
            model_name='questionasked',
            name='user',
        ),
        migrations.DeleteModel(
            name='QuestionAsked',
        ),
    ]
