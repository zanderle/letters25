# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0010_auto_20150730_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='letter',
            name='letter_length',
            field=models.IntegerField(default=0, help_text=b'What is the approximate reading length of this letter. Leave empty for autofill.', blank=True),
            preserve_default=False,
        ),
    ]
