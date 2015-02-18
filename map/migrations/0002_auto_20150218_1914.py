# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bikes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('bikes_number', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('station', models.ForeignKey(to='map.Station', related_name='start')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tripend',
            name='station',
        ),
        migrations.DeleteModel(
            name='TripEnd',
        ),
        migrations.RemoveField(
            model_name='tripstart',
            name='station',
        ),
        migrations.DeleteModel(
            name='TripStart',
        ),
    ]
