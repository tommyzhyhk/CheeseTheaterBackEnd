# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieshow', '0003_auto_20150401_0050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theater',
            name='movies',
        ),
        migrations.AddField(
            model_name='movie',
            name='theaters',
            field=models.ManyToManyField(through='movieshow.MovieShip', to='movieshow.Theater'),
            preserve_default=True,
        ),
    ]
