# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0004_buy_ticketid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='ticketid',
        ),
        migrations.AddField(
            model_name='buy',
            name='ticket',
            field=models.ManyToManyField(to='ticket.Ticket'),
        ),
    ]
