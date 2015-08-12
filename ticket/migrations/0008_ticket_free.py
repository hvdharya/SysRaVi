# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20150811_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='free',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
