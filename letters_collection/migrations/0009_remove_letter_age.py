# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0008_auto_20150730_2338'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='letter',
            name='age',
        ),
    ]
