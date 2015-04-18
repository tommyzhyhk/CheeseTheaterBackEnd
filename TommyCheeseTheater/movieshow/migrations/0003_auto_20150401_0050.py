# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieshow', '0002_cheeseuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieShip',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('tickets', models.PositiveIntegerField()),
                ('movie', models.ForeignKey(to='movieshow.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Theater',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('movies', models.ManyToManyField(through='movieshow.MovieShip', to='movieshow.Movie')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='movieship',
            name='theater',
            field=models.ForeignKey(to='movieshow.Theater'),
            preserve_default=True,
        ),
    ]
