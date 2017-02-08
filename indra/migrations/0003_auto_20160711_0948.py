# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indra', '0002_auto_20160711_0905'),
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
