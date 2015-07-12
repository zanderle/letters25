# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0002_letter_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='timestamp_published',
            field=models.DateTimeField(help_text=b'When was this letter published (leave empty for auto-fill)', null=True, blank=True),
        ),
    ]
