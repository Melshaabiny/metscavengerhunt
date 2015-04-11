# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0003_auto_20150406_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='area_of_expertise',
            field=models.CharField(max_length=30, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='expert_level',
            field=models.CharField(default=b'beginner', max_length=15, blank=True, choices=[(b'expert', b'Expert'), (b'itermmediate', b'Intermmediate'), (b'beginner', b'Beginner')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.ImageField(upload_to=b'user_auth/user_pic/', blank=True),
            preserve_default=True,
        ),
    ]
