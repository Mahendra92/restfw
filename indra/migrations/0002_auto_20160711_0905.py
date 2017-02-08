# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('indra', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='id',
        ),
        migrations.AddField(
            model_name='bus',
            name='passenger_id',
            field=models.UUIDField(default=uuid.uuid4, serialize=False, editable=False, primary_key=True),
        ),
    ]
