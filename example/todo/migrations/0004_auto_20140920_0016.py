# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_auto_20140919_2201'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.CharField(default=b'Do Now', max_length=32, choices=[(b'Do Now', b'Do Now'), (b'Later', b'later')]),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='todo',
            name='link',
            field=models.URLField(default=None, null=True, blank=True),
            preserve_default=True,
        ),
    ]
