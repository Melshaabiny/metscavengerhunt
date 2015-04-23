# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_remove_userinfo_when_registered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='picture',
            field=models.ImageField(upload_to=b'user_auth/user_pic/'),
            preserve_default=True,
        ),
    ]
