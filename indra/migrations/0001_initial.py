# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('passenger_name', models.CharField(max_length=50)),
                ('mail_id', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('arrival', models.CharField(max_length=30)),
                ('destination', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
            ],
        ),
    ]
