# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0002_auto_20150810_0142'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='buy',
            name='ticket',
        ),
    ]
