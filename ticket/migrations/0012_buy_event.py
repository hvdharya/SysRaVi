# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
        ('ticket', '0011_auto_20150812_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='event',
            field=models.ForeignKey(default=0, to='event.Event'),
            preserve_default=False,
        ),
    ]
