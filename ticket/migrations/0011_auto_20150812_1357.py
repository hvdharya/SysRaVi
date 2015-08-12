# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0010_auto_20150812_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='buy',
            field=models.ForeignKey(null=True, to='ticket.Buy'),
        ),
    ]
