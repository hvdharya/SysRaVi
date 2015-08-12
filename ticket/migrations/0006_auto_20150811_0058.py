# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_auto_20150811_0048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='ticket',
        ),
        migrations.AddField(
            model_name='buy',
            name='ticket',
            field=models.ForeignKey(default=0, to='ticket.Ticket'),
            preserve_default=False,
        ),
    ]
