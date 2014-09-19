# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'What do you need to do?', max_length=255)),
                ('description', models.TextField(help_text=b'How are you going to do it?')),
                ('due_date', models.DateTimeField(default=None, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
