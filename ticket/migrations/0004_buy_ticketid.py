# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0003_remove_buy_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='ticketid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
