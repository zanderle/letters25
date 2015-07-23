# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0004_auto_20150717_1443'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='popularity_index',
            field=models.IntegerField(default=0, help_text=b'The letter with higher index, will be shown as more popular.         (This is only a temporary measure, until I automate it)', blank=True),
        ),
    ]
