# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '__first__'),
        ('account', '__first__'),
        ('ticket', '0012_buy_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('number', models.IntegerField()),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to='account.User')),
            ],
        ),
    ]
