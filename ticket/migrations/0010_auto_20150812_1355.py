# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0009_auto_20150811_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='eventid',
            new_name='event',
        ),
        migrations.RemoveField(
            model_name='buy',
            name='event',
        ),
        migrations.AddField(
            model_name='ticket',
            name='buy',
            field=models.OneToOneField(null=True, to='ticket.Buy'),
        ),
    ]
