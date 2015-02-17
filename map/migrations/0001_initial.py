# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=128, unique=True)),
                ('latitude', models.DecimalField(max_digits=12, decimal_places=9)),
                ('longitude', models.DecimalField(max_digits=12, decimal_places=9)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripEnd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('time', models.DateTimeField()),
                ('station', models.ForeignKey(to='map.Station', related_name='end')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TripStart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('time', models.DateTimeField()),
                ('station', models.ForeignKey(to='map.Station', related_name='start')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
