# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_auto_20150218_1914'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bike',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('number_of_bikes', models.IntegerField()),
                ('time', models.DateTimeField()),
                ('station', models.ForeignKey(related_name='start', to='map.Station')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='bikes',
            name='station',
        ),
        migrations.DeleteModel(
            name='Bikes',
        ),
    ]
