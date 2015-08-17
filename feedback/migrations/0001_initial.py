# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '__first__'),
        ('event', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('rate', models.IntegerField()),
                ('comment', models.CharField(max_length=160)),
                ('event', models.ForeignKey(to='event.Event')),
                ('user', models.ForeignKey(to='account.User')),
            ],
        ),
    ]
