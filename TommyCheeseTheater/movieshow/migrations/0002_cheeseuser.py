# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movieshow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheeseUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=75, db_index=True, unique=True)),
                ('password', models.CharField(max_length=20, db_index=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
