# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('letters_collection', '0005_letter_popularity_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='timestamp_published',
            field=models.DateTimeField(default=django.utils.timezone.now, help_text=b'When was this letter published (leave empty for auto-fill)', blank=True),
        ),
    ]
