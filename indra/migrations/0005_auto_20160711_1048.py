# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indra', '0004_auto_20160711_1010'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='passenger_id',
        ),
        migrations.AlterField(
            model_name='bus',
            name='passenger_name',
            field=models.CharField(max_length=50, serialize=False, primary_key=True),
        ),
    ]
