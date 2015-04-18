# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('detail', models.CharField(blank=True, max_length=255)),
                ('image', models.CharField(blank=True, max_length=255)),
                ('money', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255)),
                ('year', models.CharField(blank=True, max_length=255)),
                ('number', models.IntegerField()),
            ],
            options={
                'db_table': 'Movie',
            },
            bases=(models.Model,),
        ),
    ]
