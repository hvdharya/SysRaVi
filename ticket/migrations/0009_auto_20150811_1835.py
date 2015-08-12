# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_ticket_free'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='ticket',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='eventid',
            field=models.ForeignKey(to='event.Event'),
        ),
    ]
