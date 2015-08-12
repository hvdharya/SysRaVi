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
            name='Buy',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('purches_id', models.IntegerField()),
                ('trace_id', models.IntegerField()),
                ('event', models.OneToOneField(to='event.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('price', models.FloatField()),
                ('type', models.CharField(max_length=100)),
                ('seat_num', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='buy',
            name='ticket',
            field=models.ManyToManyField(to='ticket.Ticket'),
        ),
        migrations.AddField(
            model_name='buy',
            name='user',
            field=models.OneToOneField(to='account.User'),
        ),
    ]
