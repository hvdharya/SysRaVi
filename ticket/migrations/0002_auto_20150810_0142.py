# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buy',
            old_name='purches_id',
            new_name='purchase_id',
        ),
        migrations.AddField(
            model_name='ticket',
            name='eventid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
