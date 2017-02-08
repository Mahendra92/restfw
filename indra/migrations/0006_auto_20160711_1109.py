# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('indra', '0005_auto_20160711_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='passenger_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='passenger_name',
            field=models.CharField(max_length=50),
        ),
    ]
