# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20150811_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='event',
            field=models.ForeignKey(to='event.Event'),
        ),
        migrations.AlterField(
            model_name='buy',
            name='user',
            field=models.ForeignKey(to='account.User'),
        ),
    ]
